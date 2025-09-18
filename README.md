# serverless_web_app

**Assignment 2** - **Building a Serverless Web Application with AWS Lambda and DynamoDB** <br>
Reference - https://sjsu.instructure.com/courses/1611826/assignments/7506911

**Description**: <br>
_Steps for implementation _<br>
	1.	Set up DynamoDB Table -	Created a table named StudentRecords with student_id as the primary key. <br>
	2.	Create Lambda Function - Wrote a function StudentRecordHandler to handle CRUD operations and Granted permissions for Lambda to read/write to DynamoDB. <br>
	3.	Connect Lambda with API Gateway - Created a REST API (StudentAPI) with resources /students. <br>
	Configured methods: <br>
	•	POST → Add new student record. <br>
	•	GET → Retrieve student details. <br>
	•	(Optional) PUT → Update student details. <br>
	•	(Optional) DELETE → Delete student record. <br>
	4.	Deploy and Test API - Deployed API to a stage (e.g., /dev) and Used Postman or curl to send requests and verify records in DynamoDB. <br>
	5.	Reflection - Documented challenges faced at the end of the readme. <br>

**Implementation**:

AWS Dynamo DB Table Records (Below are the table records after few create operations):
<img width="404" height="240" alt="image" src="https://github.com/user-attachments/assets/572fbb9a-d368-467b-a19f-5b8a5591dd4b" />

<img width="796" height="481" alt="image" src="https://github.com/user-attachments/assets/6eb9de57-17f8-42c1-a2ef-19058867a9a3" />

AWS Lambda Function: 
<img width="1204" height="724" alt="image" src="https://github.com/user-attachments/assets/d66376b1-df94-49c1-a1de-b62f65b161ca" />

AWS API Gateway
<img width="1413" height="499" alt="image" src="https://github.com/user-attachments/assets/fb7fd693-82ac-4ee5-bbbd-f8a07bec2c21" />

Testing the CRUD Operations: 

1. POST (Create Student entry)
<img width="838" height="465" alt="image" src="https://github.com/user-attachments/assets/b162a567-eb00-418a-a492-b7037c626645" />

2. GET (Get Student by student_Id)
<img width="847" height="492" alt="image" src="https://github.com/user-attachments/assets/a9808126-bec3-4e07-85f0-154539acdc3f" />

3. PUT (Update the student)
<img width="836" height="484" alt="image" src="https://github.com/user-attachments/assets/9ea3785b-067c-4163-ac27-0bb25b8ec203" />

4. DELETE (Delete student entry)
<img width="847" height="447" alt="image" src="https://github.com/user-attachments/assets/52e694e7-d482-416d-9569-994ad57af4c1" />

**Reflection** <br>
Here are few challenges I faced while implementing the serverless web application.

- As I worked in a free-tier basic account, I have seen few access issues around editing stages, roles etc.. <br>
- There are few changes I had to do in the API Gateway while creating APIs for the API Gateway to accept JSON Schema requests from the client(postman, cmd, etc..).

Overall, 
I have learnt how to build a serverless web application that connects API Gateway → AWS Lambda → DynamoDB, learned how to perform basic CRUD operations (Create, Read, Update, Delete) on DynamoDB using Lambda, deployed and tested an API endpoint that can be called from tools like Postman or curl and gained hands-on experience with serverless architecture and AWS services.

