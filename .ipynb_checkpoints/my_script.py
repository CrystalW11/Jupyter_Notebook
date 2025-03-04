from IPython.core.display import display, HTML, Javascript

display(
    HTML(
        """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>JavaScript and Python Interaction</title>
</head>
<body>
  <h2>Click the button to trigger a JavaScript alert:</h2>
  <button onclick="sayHello()">Click Me</button>

  <script type="text/javascript">
    function sayHello() {
      alert('Hello from JavaScript!');
    }
  </script>
</body>
</html>
"""
    )
)
