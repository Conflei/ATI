var myObj = {
    duration:"5000",
    easing:"swing",
    css_class:"cualquierCosa",
    links: [
        {
            text:"GameSpot",
            href:"http://www.gamespot.com/"
        },
        {
            text:"Pinterest",
            href:"https://www.pinterest.com/"
        },
        [
            {
                text:"Operating Systems",
                href:"#"
            },
            {
                text:"Debian", 
                href:"https://www.debian.org/"
            },
            {
                text:"CentOS",
                href:"https://www.centos.org/"
            },
            {
                text:"FreeBSD",
                href:"https://www.freebsd.org/"
            },
            {
                text:"Slax",
                href:"http://www.slax.org/"
            }
        ],
        {
            text:"9gag",
            href:"http://9gag.com/"
        },
        [
            {
                text:"Video Cards",
                href:"#"
            },
            {
                text:"NVIDIA",
                href:"http://www.nvidia.com/page/home.html"
            },
            {
                text:"AMD",
                href:"http://www.amd.com/en-us"
            }
        ]
    ]
};

$.fn.greenify = function()
{
	this.css("color", "green");
};

function test()
{
		$("a").greenify();	
		alert("what");
}


$(document).ready(function(){

		$.fn.ati_noseque(myObj);
						
});

$(document).ready(function(){

		$('.dropdown').hover(
				function(){
					$(this).children('.sub-menu').slideDown(200);
				},

				function(){
					$(this).children('.sub-menu').slideUp(200);
				}

			);

});

$.fn.ati_noseque = function(att){
		var list = $("ul");

		var settings = $.extend({
			duration:4000,
			easing:"swing",
			css_class:"myClass",
			links:[
				'#',
				'#',
				'#',
				'#'
			]
			}, att);

			for(i = 0; i<settings.links.length; ++i)
			{
				if(settings.links[i].text != null)
				{
					console.log(settings.links[i].text);
					list.append("<li><a target = \"_blank\"  href=\""+settings.links[i].href+" \"> "+settings.links[i].text+"</li>");
				}
				else
				{
					var dropObj = $("<li>");
					dropObj.attr("class","dropdown");
					
					var fathera =  $("<a>");
					fathera.attr("target","_blank");
					fathera.attr("href",settings.links[i][0].href);
					fathera.append(settings.links[i][0].text);
					var subMenu = $("<ul>");
					subMenu.attr("class","sub-menu");

							for(j = 1; j<settings.links[i].length; ++j)
							{
								var sonLi = $("<li></li>");
								var sonA = $("<a>");
								sonA.attr("target","_blank");
								sonA.attr("href",settings.links[i][j].href);
								sonA.append(settings.links[i][j].text);
								sonLi.append(sonA);
								subMenu.append(sonLi);
							}
							dropObj.append(fathera);
							dropObj.append(subMenu);
							list.append(dropObj);
				}
			}
}

