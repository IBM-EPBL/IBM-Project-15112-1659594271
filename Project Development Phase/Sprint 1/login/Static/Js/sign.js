function validateform(){  
    var nameRegex = /^[a-zA-Z\-]+$/;
    var username = document.sign.username.value.match(nameRegex); 
    var password=document.sign.password.value; 
    
      
   
        
    if(username == null){
        alert("Enter a Valid username");
        document.sign.username.focus();
        return false;
    }
    else if(password.length<8){  
      alert("Password must be at least 8 characters long.");  
      return false;  
      }  
    }  

