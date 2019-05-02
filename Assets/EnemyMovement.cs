using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyMovement : MonoBehaviour {
    private int health = 20;
    

    // Use this for initialization
    void Start () {
        
        transform.Translate(new Vector3(0, 0, 1) * Time.deltaTime);

        //If the enemy hits a wall, it changes direction
        /*
        void OnCollisionEnter(Collision col)
        {
            
            if (col.gameObject.name == "Wall")
            {
                Destroy(OnCollisionEnter.gameObject);
                //Invoke("Attack", 2);
            }
            
    }

        //If the enemy's health reaches zero it dies
        if (health == 0)
            Destroy(gameObject);
            */

    }

    // Update is called once per frame
    void Update () {

        
	}
}
