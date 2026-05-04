using UnityEngine;
using UnityEngine.InputSystem;

public class Playermove : MonoBehaviour
{
    public Vector2 inputVec;
    public float speed;
    public GameObject arrowPrefab;
    public Sprite arrowSprite;
    public Transform firePoint;
    public float arrowSpawnDistance = 0.5f;
    public float arrowSpeed = 10f;
    public float arrowLifeTime = 3f;

    Rigidbody2D rigid;
    Animator anim;
    SpriteRenderer spriter;
    bool facingRight = true;

    void Awake()
    {
        rigid = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
        spriter = GetComponent<SpriteRenderer>();
    }

    void FixedUpdate()
    {
        Vector2 nextVec = inputVec * speed * Time.fixedDeltaTime;
        rigid.MovePosition(rigid.position + nextVec);
    }

    void OnMove(InputValue value)
    {
        inputVec = value.Get<Vector2>();
    }

    void OnAttack(InputValue value)
    {
        Debug.Log("OnAttack called!");
        ShootArrow();
    }

    private void ShootArrow()
    {
        Vector2 shootDirection = GetShootDirection();
        Vector3 spawnPosition = firePoint != null
            ? firePoint.position
            : transform.position + (Vector3)shootDirection * arrowSpawnDistance;

        if (arrowPrefab != null)
        {
            Debug.Log("Arrow spawning at position: " + spawnPosition + " direction: " + shootDirection);
            GameObject arrow = Instantiate(arrowPrefab, spawnPosition, Quaternion.identity);
            ConfigureArrow(arrow, shootDirection);
            return;
        }

        if (arrowSprite == null)
        {
            Debug.LogWarning("Arrow prefab and arrow sprite are not assigned on " + name);
            return;
        }

        Debug.Log("Arrow spawning at position: " + spawnPosition + " direction: " + shootDirection);
        GameObject arrowObject = CreateArrowFromSprite(spawnPosition);
        ConfigureArrow(arrowObject, shootDirection);
    }

    private GameObject CreateArrowFromSprite(Vector3 spawnPosition)
    {
        GameObject arrowObject = new GameObject("ArrowDynamic");
        arrowObject.transform.position = spawnPosition;

        SpriteRenderer spriteRenderer = arrowObject.AddComponent<SpriteRenderer>();
        spriteRenderer.sprite = arrowSprite;
        spriteRenderer.sortingOrder = 10;

        Rigidbody2D arrowRb = arrowObject.AddComponent<Rigidbody2D>();
        arrowRb.bodyType = RigidbodyType2D.Kinematic;
        arrowRb.sharedMaterial = null;

        BoxCollider2D collider = arrowObject.AddComponent<BoxCollider2D>();
        collider.isTrigger = true;

        arrowObject.AddComponent<ArrowProjectile>();
        return arrowObject;
    }

    private void ConfigureArrow(GameObject arrow, Vector2 shootDirection)
    {
        IgnorePlayerCollision(arrow);

        ArrowProjectile projectile = arrow.GetComponent<ArrowProjectile>();
        if (projectile != null)
        {
            projectile.SetDirection(shootDirection);
            projectile.speed = arrowSpeed;
            projectile.lifetime = arrowLifeTime;
            return;
        }

        Rigidbody2D arrowRb = arrow.GetComponent<Rigidbody2D>();
        if (arrowRb != null)
        {
            arrowRb.linearVelocity = shootDirection * arrowSpeed;
        }
    }

    private void IgnorePlayerCollision(GameObject arrow)
    {
        Collider2D arrowCollider = arrow.GetComponent<Collider2D>();
        if (arrowCollider == null) return;

        Collider2D[] playerColliders = GetComponents<Collider2D>();
        foreach (var playerCollider in playerColliders)
        {
            if (playerCollider != null)
            {
                Physics2D.IgnoreCollision(arrowCollider, playerCollider);
            }
        }
    }

    private Vector2 GetShootDirection()
    {
        if (inputVec.sqrMagnitude > 0.01f)
        {
            return inputVec.normalized;
        }
        return facingRight ? Vector2.right : Vector2.left;
    }

    private void LateUpdate()
    {
        anim.SetFloat("Speed", inputVec.magnitude);
        if (inputVec.x != 0)
        {
            spriter.flipX = inputVec.x < 0;
            facingRight = inputVec.x > 0;
        }
    }

}
