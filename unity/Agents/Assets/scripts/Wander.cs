using UnityEngine;
public class Wander : MonoBehaviour {
    private Vector3 targetPosition;

    private float movementSpeed = 5.0f;
    private float rotationSpeed = 2.0f;
    private float targetPositionTolerance = 3.0f;
    private float minX;
    private float maxX;
    private float minZ;
    private float maxZ;

    private float currentY;

    void Start() {
    
        minX = -45;
        maxX = 53;

        minZ = -26;
        maxZ = 73;

        currentY = transform.position.y;
        //Get Wander Position
        GetNextPosition();
    }

    void Update() {
        if (Vector3.Distance(targetPosition, transform.position) <= targetPositionTolerance){

            GetNextPosition();
            
        }

        Quaternion tarRot = Quaternion.LookRotation(targetPosition - transform.position);
        transform.rotation = Quaternion.Slerp(transform.rotation, tarRot, rotationSpeed * Time.deltaTime);
        transform.Translate(new Vector3(0, 0, movementSpeed * Time.deltaTime));
        

        
    }

    void GetNextPosition() 
    {
        targetPosition = new Vector3(Random.Range(minX, maxX), currentY, Random.Range(minZ, maxZ));
        
    }
}