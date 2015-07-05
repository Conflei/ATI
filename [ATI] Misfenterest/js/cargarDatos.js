$(document).ready(function()
{	
	
	generation();
	
});


function generation() {

	
	var n;
	if(cant<toadd.length)
	{
	
		
		for(var i=1; i<=4&&cant<toadd.length; i++)
		{
			n = 150+Math.floor((Math.random() * 130) + 1);

		  	cont = '<div class ="row sombraImagen" style = "background-color: white; margin-left:1px; margin-top:5%; border-radius: 4px;">';
		    cont +=      '<a href="#" style ="border-radius: 4px" onclick = "mostrarImagen('+cant+')">';
		    cont +=          '<img  width="100%" height="'+n+'px" src="'+ urlImg(cant) +'" class="img-rounded"/>'
		    cont +=      '</a>'
		    cont +=    '<div class="caption">'
		    cont +=         '<h3>'+title(cant)+'</h3>'
		    cont +=          '<p>'+description(cant)+'</p>'
		    cont +=    '</div>'
		    cont +='</div>';  
		    cant = cant + 1;
		    $("#content"+i).append(cont);

		}
		
	}
 }

$(window).scroll(function(){
	if ($(window).scrollTop() == $(document).height() - $(window).height()){
		//pagina++;
		generation();
	}					
});