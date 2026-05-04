using UnityEngine;

public class ArrowProjectile : MonoBehaviour
{
    public float speed = 10f;
    public float lifetime = 3f;
    public Vector2 direction = Vector2.right;

    Rigidbody2D rigid;

    void Awake()
    {
        rigid = GetComponent<Rigidbody2D>();
    }

    void Start()
    {
        Debug.Log("ArrowProjectile spawned! Direction: " + direction + ", Speed: " + speed);
        if (rigid != null)
        {
            rigid.linearVelocity = direction.normalized * speed;
            Debug.Log("Velocity set to: " + rigid.linearVelocity);
        }
        else
        {
            Debug.LogWarning("Rigidbody2D is null!");
        }
        Destroy(gameObject, lifetime);
    }

    public void SetDirection(Vector2 dir)
    {
        if (dir.sqrMagnitude > 0.01f)
        {
            direction = dir.normalized;
            float angle = Mathf.Atan2(direction.y, direction.x) * Mathf.Rad2Deg;
            transform.rotation = Quaternion.Euler(0f, 0f, angle);
        }
    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.attachedRigidbody != null && other.attachedRigidbody.gameObject != gameObject)
        {
            Destroy(gameObject);
        }
    }
}
