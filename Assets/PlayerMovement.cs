using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class PlayerMovement : MonoBehaviour {

    // Use this for initialization
    void Start() { }
    public float moveSpeed = 20f;
    public float health = 20f;
    public Rigidbody rb;
    //return the forward speed
    //return the sid}eways speed
    public float sideWaysForce = 500f;
    void FixedUpdate() {
        //If the Arrow Keys keys are pressed, move around
        if (Input.GetKey(KeyCode.Space))
            transform.Translate(Vector3.up * moveSpeed * Time.deltaTime);
        if (Input.GetKey(KeyCode.UpArrow))
            transform.Translate(Vector3.forward * moveSpeed * Time.deltaTime);
        if (Input.GetKey(KeyCode.LeftArrow))
            transform.Translate(Vector3.left * moveSpeed * Time.deltaTime);
        if (Input.GetKey(KeyCode.RightArrow))
            transform.Translate(Vector3.right * moveSpeed * Time.deltaTime);
        if (Input.GetKey(KeyCode.DownArrow))
            transform.Translate(-Vector3.forward * moveSpeed * Time.deltaTime);


        /*
        //If the player bumps into an enemy, a battle will iniatate
        void OnCollisionEnter(Collision col) {
            if (OnCollisionEnter.gameObject.name == "Player Character")
            {
                Destroy(col.gameObject);
                //Invoke("Attack", 2);
            }
        }
        */
        //If the player's health reaches 0, they die
        if (health == 0)
            Destroy(gameObject);
            
    }
}
    

/*
	// Update is called once per frame
	void Update () {
		
	}
*/