$(document).ready(function()
{	
	generationUP();
	
});

$(window).scroll(function(){
	if ($(window).scrollTop() == $(document).height() - $(window).height()){
		generationUP();
	}					
});

function generationUP() {

	images = doAjaxPage("upload");
	
	if(images && images != undefined && images != "fallo"){
		//alert(images[i]["picdir"] + images[i]["title"] + images[i]["description"] + images[i]["author"]);
		alert(images.length);
		for(var i=0; i<images.length; i++){
			n = 150+Math.floor((Math.random() * 130) + 1);

		  	cont = '<div class ="row sombraImagen" style = "background-color: white; margin-left:1px; margin-top:5%; border-radius: 4px;">';
		    cont +=      '<a href="#" style ="border-radius: 4px" onclick = "mostrarImagen('+cant+')">';
		    cont +=          '<img  width="100%" height="'+n+'px" src="'+ images[i]["picdir"] +'" class="img-rounded"/>'
		    cont +=      '</a>'
		    cont +=    '<div class="caption">'
		    cont +=         '<h3>'+images[i]["title"]+'</h3>'
		    cont +=          '<p>'+images[i]["description"]+'</p>'
		    cont +=    '</div>'
		    cont +='</div>';  
		    cant = cant + 1;
		    $("#content"+j).append(cont);
		    if(j==4){
				 j = 1;
			}
			else{
				j = j + 1;
			}

		}
		
	}
 }


