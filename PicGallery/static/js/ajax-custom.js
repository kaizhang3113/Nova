/**
 * @author
 *
 * Custom ajax access
 */
// Host IP address
const HOST = "http://127.0.0.1:5000";
// const TEXT_HOST = "http://localhost:8080";


var storage = window.sessionStorage;

const NO_RESULT = "There's no result from the server";
const GET_METHOD = 'GET';
const POST_METHOD = 'POST';
const PUT_METHOD = 'PUT';
const DELETE_METHOD = 'delete';
const LOADING = "Loading...";


function restGet(restUrl, httpMethod, callback, resultDiv) {
  rest(restUrl, httpMethod, "", "application/json", "json", callback, resultDiv);
}

function restSet(restUrl, httpMethod, entity, callback, resultDiv) {
  rest(restUrl, httpMethod, entity, "application/x-www-form-urlencoded", "json", callback, resultDiv);
}

function rest(restUrl, httpMethod, entity, contentType, dataType, callback, resultDiv) {
  var resultLine = jQuery("#error");
  if (resultLine !== "") {
    resultLine = jQuery(resultDiv);
  }
  resultLine.html(LOADING);
  var request = jQuery.ajax({
    type: httpMethod,
    url: restUrl,
    data: entity,
    contentType: contentType,
    dataType: dataType
  }).done(function(data) {
    try {
      if (data === null || data === undefined) {
          resultLine.html(NO_RESULT);
      } else {
        // console.log("inner ajax callback...");
        callback(data);
        resultLine.html("");
      }
    } catch (e) {
      resultLine.html(e);
    }
  }).fail(function(textStatus, errorThrown) {
    resultLine.html("Load fail");
  });
}

function checkPic(upload, infoId) {
  console.log(upload.files);
  $("#"+infoId).empty().append("<li> <h4>Only Valid file(s) will be uploaded.</h4><li>");
  for(var i=0; i<upload.files.length; i++){
    var fileInput = upload.files[i];
    if(fileInput.size > 500*1024){
      $("#"+infoId).append("<li>The size of File "+ fileInput.name +" is larger than 500KB.</li>");
    } if(fileInput.type != "image/jpeg"){
      $("#"+infoId).append("<li>The format of File "+ fileInput.name +" is not JPEG.</li>");
    }
  }
}

function validPic(file){
  if(file.size > 500*1024){
    return false;
  }else if(file.type != "image/jpeg"){
    return false;
  }else{
    return true;
  }
}
