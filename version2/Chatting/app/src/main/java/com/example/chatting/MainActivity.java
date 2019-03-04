package com.example.chatting;

import android.content.Context;
import android.graphics.Color;
import android.support.constraint.ConstraintLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.ListView;
import android.widget.TextView;

import com.firebase.client.Firebase;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

import java.util.ArrayList;
import java.util.Arrays;

public class MainActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;
    private Firebase mRef;
    private Button sendData;
    private ListView listView;
    ArrayList<String> itemList;
    private ArrayAdapter<String> adapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //mAuth = FirebaseAuth.getInstance();
        Firebase.setAndroidContext(this);





        sendData=(Button)findViewById(R.id.send);
        listView = (ListView) findViewById(R.id.list_of_messages);

        String[] items={"Apple","Banana","Clementine"};
        itemList=new ArrayList<String>(Arrays.asList(items));
        adapter=new ArrayAdapter<String>(this,R.layout.list_items,R.id.txtview,itemList);
        ListView listV=(ListView)findViewById(R.id.list_of_messages);
        listV.setAdapter(adapter);



        mRef=new Firebase("https://chatting-2e9b2.firebaseio.com/");
        sendData.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                EditText et = (EditText) findViewById(R.id.message);
                String str = et.getText().toString();
                itemList.add(str);
                adapter.notifyDataSetChanged();
                et.setText("");

                Firebase mRefChild=mRef.child("Message");

                mRefChild.setValue(str);
            }
        });

    }
    public void createTextView(String sText){
        LinearLayout ll=new LinearLayout(this);

        // Create TextView
        TextView product = new TextView(this);
        product.setText(sText);
        ll.addView(product);



    }
}
