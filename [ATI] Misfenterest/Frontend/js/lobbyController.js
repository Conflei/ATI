var misObjetos = [
  {
  	"creator_id" : "Evo",
  	"description" : "Quiero compartir esta foto con ustedesasda",
    "url" : "/assets/img0.png"
  },
  {
  	"creator_id" : "Misa",
	"description" : "Quiero compartir esta foto con ustedes",
	"url" : "../assets/img1.jpg"
  },
  {
  	"creator_id" : "Shortman",
	"description" : "Quiero compartir esta foto con ustedes",
	"url" : "/assets/img2.jpg"
  },
  {
  	"creator_id" : "Cebin",
	"description" : "Quiero compartir esta foto con ustedes",
	"url" : "/assets/img3.jpg"
  },
  {
  	"creator_id" : "Yldemaro (Divino)",
	"description" : "Quiero compartir esta foto con ustedes",
	"url" : "assets/img4.jpg"
  }
];

function getDocHeight()
{
	var D = document;
	return Math.max(
			D.body.scrollHeight, D.documentElement.scrollHeight,
			D.body.offsetHeight, D.documentElement.offsetHeight,
			D.body.clientHeight, D.documentElement.clientHeight
		);
}

var body;
var mainContainer;
var grid;
var gridSizer;
var $isoGrid;
var firstFill = false;
var showingIMG = false;

var isoOptions = {
	itemSelector: '.grid-item',
  	percentPosition: true,
  	layoutMode: 'masonry',
  	masonry:{
  		columnWidth:'.grid-sizer',
  		gutter:23
  	  }
}

$(document).ready(function(){

	body = $(".allContent");

	mainContainer = $("<div>");
	mainContainer.attr("class", "mainContent");
	
	grid = $("<div>");
	grid.attr("class", "grid");

	gridSizer =  $("<div>");
	gridSizer.attr("class", "grid-sizer");

	grid.append(gridSizer);
	mainContainer.append(grid);

	body.prepend(mainContainer);
	$isoGrid = $('.grid').isotope(isoOptions);

	fill();
	firstFill = true;
	showingIMG = false;
})

$(document).ready(function(){

		$(window).scroll(function(){
			if($(window).scrollTop() + $(window).height() == getDocHeight())
			{
				if(firstFill)fill();
			}
		})

});

function UploadContent(){
	$("#myModal").modal();
}

$(document).ready(function(){
    $("#myBtn").click(function(){
        $("#myModal").modal();
    });
});


function showImage(index)
{
			$('.contenidoSelecto').slideDown('fast');
			$('.allContent').css("opacity", "0.4");
			$('#imgContent').attr("src", misObjetos[index]["url"]);
			$('h4').html(misObjetos[index]["creator_id"]);
			$('#parContent').html(misObjetos[index]["description"]);
			showingIMG = true;
};

function hideSeleccion(){
		$('.contenidoSelecto').slideUp('slow');
		$('.allContent').attr("onclick", "showImage()");
		$('.allContent').css("opacity", "1");
	
	
};

$(document).ready( function(){
	$('#cerrar').bind('click', function(){
		hideSeleccion();
	});
})



function fill()
{
		for(i = 0; i<7; i++)
		{
			var gridElement = $("<div>");
			var rand = Math.floor(Math.random()*10) % 3;
			if(rand==0) gridElement.attr("class", "grid-item grid-item--height3");
			if(rand==1) gridElement.attr("class", "grid-item grid-item--height2");
			if(rand==2) gridElement.attr("class", "grid-item");
			if(rand==3) gridElement.attr("class", "grid-item grid-item--height1");

			var elemento = $("<div>");
			elemento.attr("class", "miElemento");

			var randObject = Math.floor(Math.random()*10) % 5;
			var imagen = $("<img>");
			imagen.attr("src",'{{misObjetos[randObject]["url"]}}');
			imagen.attr("onclick", "showImage("+randObject+")");
			elemento.append(imagen);
			elemento.append("<hr>");
			elemento.append("<p>"+misObjetos[randObject]["description"]);
			elemento.append("<hr>");

			var imagenPerfil = $("<img>");
			imagenPerfil.attr("src", "assets/profile.jpg");
			imagenPerfil.attr("id", "profile");

			elemento.append(imagenPerfil);

			var link = $("<a>");
			link.attr("href", "#");
			link.attr("class", "userName");
			link.attr("id", "profileName");
			link.append(misObjetos[randObject]["creator_id"]);
			elemento.append(link);

			gridElement.append(elemento);
			$isoGrid.append(gridElement).isotope('appended', gridElement);			
		}

		
}







