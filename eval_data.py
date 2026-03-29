eval_data = [
    {"question": "What is Node.js?", "ground_truth": "Node.js is a JavaScript runtime built on the V8 engine that allows running JavaScript outside the browser."},

    {"question": "Why should Node.js be used?", "ground_truth": "Node.js is useful because it is fast, non-blocking, and suitable for scalable backend applications."},

    {"question": "What is the V8 engine?", "ground_truth": "The V8 engine is a JavaScript engine that executes JavaScript code and is used by Node.js."},

    {"question": "What is non-blocking I/O?", "ground_truth": "Non-blocking I/O allows multiple operations to run without waiting for previous ones to complete."},

    {"question": "What is a Node.js script?", "ground_truth": "A Node.js script is a JavaScript file that can be executed using the Node.js runtime."},

    {"question": "How do you run a Node.js script?", "ground_truth": "A Node.js script is run using the node command followed by the file name."},

    {"question": "What is the Node.js module system?", "ground_truth": "The module system allows loading and using built-in, custom, and third-party modules in Node.js."},

    {"question": "What does require do in Node.js?", "ground_truth": "The require function is used to import modules and access their functionality."},

    {"question": "What is module.exports?", "ground_truth": "module.exports is used to export values or functions from a module so they can be used in other files."},

    {"question": "What are core modules in Node.js?", "ground_truth": "Core modules are built-in modules provided by Node.js for tasks like file handling and HTTP requests."},

    {"question": "What is npm?", "ground_truth": "npm is a package manager used to install and manage third-party Node.js libraries."},

    {"question": "What does npm init do?", "ground_truth": "npm init initializes a project and creates a package.json file."},

    {"question": "What is package.json?", "ground_truth": "package.json is a file that stores project metadata and dependencies."},

    {"question": "What is node_modules?", "ground_truth": "node_modules is a directory where installed npm packages are stored."},

    {"question": "What is JSON?", "ground_truth": "JSON is a lightweight data format used for storing and transferring structured data."},

    {"question": "What does JSON.stringify do?", "ground_truth": "JSON.stringify converts a JavaScript object into a JSON string."},

    {"question": "What does JSON.parse do?", "ground_truth": "JSON.parse converts a JSON string into a JavaScript object."},

    {"question": "What are command line arguments in Node.js?", "ground_truth": "Command line arguments are inputs passed to a Node.js program via the terminal."},

    {"question": "What is process.argv?", "ground_truth": "process.argv is an array that contains command line arguments passed to a Node.js application."},

    {"question": "What is Yargs?", "ground_truth": "Yargs is a library used to parse and manage command line arguments in Node.js."},

    {"question": "What is debugging in Node.js?", "ground_truth": "Debugging is the process of identifying and fixing errors in a Node.js application."},

    {"question": "What is console.log used for?", "ground_truth": "console.log is used to print output to the terminal for debugging or logging."},

    {"question": "What is asynchronous programming?", "ground_truth": "Asynchronous programming allows tasks to run without blocking the execution of other code."},

    {"question": "What is setTimeout?", "ground_truth": "setTimeout is a function that executes a callback after a specified delay."},

    {"question": "What is a callback function?", "ground_truth": "A callback function is a function passed as an argument to another function and executed later."},

    {"question": "Why are callbacks used?", "ground_truth": "Callbacks are used to handle asynchronous operations and execute code after a task is completed."},

    {"question": "What is the event loop?", "ground_truth": "The event loop is a mechanism that manages execution of asynchronous operations in Node.js."},

    {"question": "What is the call stack?", "ground_truth": "The call stack is a structure that tracks function execution in a program."},

    {"question": "What is the callback queue?", "ground_truth": "The callback queue stores functions that are ready to be executed after asynchronous operations complete."},

    {"question": "What is an HTTP request?", "ground_truth": "An HTTP request is a message sent from a client to a server to retrieve or send data."}
]