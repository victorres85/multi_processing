# Multi-Process Project
This multi-process project is built with a Test-Driven Development (TDD) approach, ensuring robustness and reliability.

## Running and Visualizing Tests
### Running Tests
1. Clone the Project:
Clone this project to your local machine.

2. Navigate to Project Root:
Open your terminal and navigate to the root directory of the project.

3. Set Permissions:
Run the following command to make the test script executable:
```
chmod +x ./run_test.sh
```

4. Run Tests:
Execute the following command in the terminal to run the tests and generate HTML reports (which will be saved in the test_reports directory):

```
./run_test.sh
```

### Visualizing Test Reports
1. Initialize Node.js Server:
Navigate to the report_app directory using the terminal.

2. Initialize Node.js Project:
Run the following commands to initialize the Node.js project and install required packages:

```
npm init -y
npm install
```

3. Start Server:
Launch the Node.js server by running the command:

```
nodemon app.js
```

4. Access Test Reports:
Open your web browser and navigate to the following URL:

<http://localhost:3000/>

This will allow you to visualize the test reports conveniently.

By following these steps, you can efficiently run tests and visualize their reports for comprehensive analysis.