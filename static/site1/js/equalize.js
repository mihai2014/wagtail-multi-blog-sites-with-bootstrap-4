//equalize width pv code divs	  
//$(document).ready(function(){

function equalize(){
    two_columns_block = document.getElementsByClassName("block-two_columns");

    for(var i = 0; i < two_columns_block.length; i++) {
      arr1 = []
      arr2 = []
	    
      var section = two_columns_block[i]; 
      var div_class_row = section.childNodes[1];

      /* 1st col-md-6 */	    
      var div = div_class_row.childNodes[1]; 
      var div_dj_code = div.childNodes[1];   
      //arr.push(div);	    
      for (let j = 0; j < div_dj_code.childNodes.length; j++) { 
	  if(div_dj_code.childNodes[j].tagName != undefined ){ 
	      div_zone = div_dj_code.childNodes[j]; 
              div_code = div_zone.childNodes[1]; 
              //alert(div_code.getAttribute("id"));
              arr1.push(div_code);
          }		  
      } 

      /* 2nd col-md-6 */	    
      var div = div_class_row.childNodes[3]; 
      var div_dj_code = div.childNodes[1];   
      //arr.push(div);      
      for (let j = 0; j < div_dj_code.childNodes.length; j++) { 
          if(div_dj_code.childNodes[j].tagName != undefined ){ 
              div_zone = div_dj_code.childNodes[j]; 
              div_code = div_zone.childNodes[1]; 
              //alert(div_code.getAttribute("id"));
              arr2.push(div_code);
          }               
      } 

      for (var k = 0; k < 3; k++) {  
          var height1 = arr1[k].clientHeight    //.style.height;
	  var height2 = arr2[k].clientHeight    //.style.height;
	  //alert(height1+ " " + height2);  
	  //??!!     
	  if(height1 > height2) 
	      arr2[k].clientHeight = height1;
	      //arr2[k].style.height = height1;
	  if(height1 < height2) 
	      arr1[k].clientHeight = height2;    
	      //arr1[k].style.height = height2;
	  
      }	      
    }

}	

//});
