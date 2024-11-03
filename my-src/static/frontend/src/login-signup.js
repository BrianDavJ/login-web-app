const PORT = "http://localhost:5000";
const termsAndCond = document.getElementsByClassName('termsAndCond')

export function checkLogin(emailOrUser, password) {
  fetch(`${PORT}/login`, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ emailOrUser, password })
  })
  .then(async (res) => {
      if (!res.ok) {
          const errorData = await res.json();
        throw new Error(errorData.error);
      }
      return res.json();
  })
  .then((data) => {
      console.log("Login successful, token: ", data.token);
  })
  .catch((error) => 
  {
    alert("Login failed: " + error.message);
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
      const checkbox = document.getElementById('checkTerms');
      if (!checkbox.checked) {
        throw new Error('You must agree to the terms and conditions before proceeding');
    }
      if (!res.ok) {
          const errorData = await res.json();
        throw new Error(errorData.error);
      }
      return res.json();
  })
  .then((data) => {
      console.log("Signup successful: ", data.message);
  })
  .catch((error) => {
      alert("Signup failed: "+ error.message);
  });
}
