$(document).ready(function(){

	console.log("init");
	var app_id = '688571277942632';
	var scopes = 'email, user_friends, public_profile';

	var btn_login = '<a id="fbLogin" href="lobby.html"><img src = "img/Facebook.png" width="5%"; height="5%;"></a>';

	var div_session = "<div id='facebook-session'>"+
	"<strong></strong>"+"<img>"+ 
	'<a id="fbLogout" href="lobby.html"><img src = "img/Facebook.png" width="5%"; height="5%;"></a>'+
	"</div>";

	var lognamestr = "<input type='text' id='logname' name='Name' required>";
	var logpassstr = "<input type='text' id='logpass' name='Name' required>";


	 window.fbAsyncInit = function() {
		 	console.log('fbAsyncInit');
		  FB.init({
		    appId      : app_id,
		    status 	   : true,
		    cookie     : true,  
		    xfbml      : true,  
		    version    : 'v2.2' 
		  });


		  FB.getLoginStatus(function(response) {
		    statusChangeCallback(response, function(){

		  	  });
	  	});

	};

  var statusChangeCallback = function (response, callback) {
    console.log(response);

    if (response.status === 'connected') {
    	getFacebookData();
    } else {
    	callback(false);
    }
  }

  var checkLoginState = function(callback) {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response, function(data){
      		callback(data);
		  	  });
    });
  }

  var getFacebookData = function(){
  	//UPDATE THIS SHIEEEEET
  	FB.api('/me', function(response){
  		console.log(response);
  		var logname = document.getElementById("logname");
  		logname.after("<input type='text' id='logname' name='Name' value='"+response.name+"' required>");
  		logname.remove();
  		//$('#logname').text(response.name);
  		//$('#logpass').text("facebook");
  	})
  }

  var facebookLogin = function() {
  	checkLoginState(function(response){
  		if(!response){
  			FB.login(function(response){
  				if(response.status === 'connected')
  					getFacebookData();
  			}, {scope: scopes});
  		}
  	})
  }

  $(document).on('click', '#fbLogin', function(e){
  	console.log("Facebook Login");
  	e.preventDefault();

  	facebookLogin();
  })

})