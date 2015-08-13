$(document).ready(function(){

	console.log("init");
	var app_id = '688571277942632';
	var scopes = 'email, user_friends, public_profile';


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
					FB.logout(function(response) {
        		//	 Person is now logged out
    					});
		  	  });
	  	});

	};

  var statusChangeCallback = function (response, callback) {
    console.log(response);

    if (response.status === 'connected') {
    	//getFacebookData();
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
		FB.api('/me', function(response){
			console.log("facebook real");
			console.log(response);
				window.location.assign("/FacebookLogin?name="+response.name+"&password=facebook");
			});
  }

	var getFacebookDataReal = function(){

	};

  var facebookLogin = function() {
  	checkLoginState(function(response){
  		if(!response){
  			FB.login(function(response){
					console.log("Status"+response.status);
  				if(response.status == 'connected')
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
