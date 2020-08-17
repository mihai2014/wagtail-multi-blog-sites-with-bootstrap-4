/* setting csrf for forms generated dynamicaly, so can not use directly {% csrf_token %}
 * 1st include in body {% csrf_token %} or use : https://github.com/js-cookie/js-cookie/
 * 2nd append script below which will clone in form the csrf token 
 * */
/* 
 <script>
 document.getElementsByTagName("body")[0].onload = function() {
     csrf_in_form("formId");    
 };
 </script>
*/

function csrf_in_form(id){ 
    try {
        var csrfValue =  document.getElementsByName("csrfmiddlewaretoken")[0].value; 
    }
    catch(err) {}

    if(csrfValue == undefined) {   
        try {
            var csrfValue = Cookies.get('csrftoken'); 
        }
        catch(err) {
            console.log("Add {% csrf_token %} in template or use js cookie library!")
            return;
        }
    }
  
    var csrfToken = document.createElement("input");
    csrfToken.setAttribute("type","hidden");
    csrfToken.setAttribute("name","csrfmiddlewaretoken");
    csrfToken.setAttribute("value",csrfValue);

    var form = document.getElementById(id); 
    form.appendChild(csrfToken);
}

