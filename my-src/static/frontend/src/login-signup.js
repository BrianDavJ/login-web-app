const PORT = "http://localhost:5000";
export function checkLogin(email, password) {
  fetch(`${PORT}/login`, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ email, password })
  })
  .then(async (res) => {
      if (!res.ok) {
          const errorData = await res.json();
        throw new Error(errorData.error);
      }
      return res.json();
  })
  .then((data) => {
      console.log("Login successful, token:", data.token);
  })
  .catch((error) => 
  {
    alert("Login failed:", error.message);
    console.error("Login failed:", error.message);
  })
   
  
};

export function registerUser(username, email, password) {
  fetch(`${PORT}/signup`, {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify({ username, email, password })
  })
  .then(async (res) => {
      if (!res.ok) {
          const errorData = await res.json();
        throw new Error(errorData.error);
      }
      return res.json();
  })
  .then((data) => {
      console.log("Signup successful:", data.message);
  })
  .catch((error) => {
      alert("Signup failed:", error.message);
      console.error("Signup failed:", error.message);
  });
}
