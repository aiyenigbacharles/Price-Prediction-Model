function onClickedEstimatedPrice(){
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
        if(uiBathrooms[i].checked) {
            return parseInt(i)+1;
        }
    }
    return -1;
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // The above functions iterate through the buttons and return the values
  }
    function onClickedEstimatedPrice() {
        console.log("Estimated price button clicked");
        var sqft = document.getElementById("uilocations");
        var bathrooms = document.getElemenbtById("uiEstimatedPrice");
        var estPrice = document.getElementById("uiEstimatedPrice")

        var url = "http://127.0.0.1:5000/predict_home_price"; //url for the price prediction endpoint

        $.post(url, { //This is a jquery POST call that makes a POST call to the url, we will get our output back in 'data'
            total_sqft: parseFloat(sqft.value),
            bhk: bhk,
            bath: bathrooms,
            location: location.value
        },function(data, status) {
            console.log(data.estimated_price);
            estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
            console.log(status)
        }
        )

    }
function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names"; //Here we make our HTTP Call
    $.get(url,function(data, status) { //This is a jquery GET call that makes a GET call to the url, we will get our response back in the 'data'
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations; //This will be our list of locations
            var uilocations = document.getElementById("uilocations"); 
            $("#uilocations").empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $("#uilocations").append(opt);
            } //The above goes through our locations one by one and adds them to our dropdown
        }
    });
 
}

window.onload = onPageLoad; //This will be used to load our HTML page and load the locations




