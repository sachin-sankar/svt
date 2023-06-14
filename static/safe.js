function login(){
    var password = sessionStorage.getItem('password')
    
    if ( password == null){
      password = prompt('Enter Password')
    }
    fetch('https://svt.sachins5.repl.co/verify',{method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({pw:password})}).then(response => {
      if (response.ok) {
        sessionStorage.setItem('password',password)
        document.getElementById('overlay').hidden = true
      }
      else{
        alert('Wrong Password')
        
      }
    })
  }