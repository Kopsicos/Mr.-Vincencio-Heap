using UnityEngine;
using System.Collections;

//put this component on camera
//drag target object (ball) onto the TargetObject public variable
public class CameraFollowObject : MonoBehaviour
{
    public Transform target;

    public float smoothedSpeed = 0.125f;
    public Vector3 offset;

    private void FixedUpdate()
    {
        Vector3 desiredPosition = target.position + offset;
        Vector3 smoothedPosition = Vector3.Lerp(transform.position, desiredPosition, smoothedSpeed);
        transform.position = smoothedPosition;

        transform.LookAt(target);
    }
}
