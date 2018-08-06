// Function that make an array from table tintas.
function makeArrayFromTable(){
  var myTableArray = [];
  $("table#makeEditable tr").each(function() {
      var arrayOfThisRow = [];
      var tableData = $(this).find('td');
      if (tableData.length > 0) {
          tableData.each(function() {if ($(this).text().trim() != "") {arrayOfThisRow.push($(this).text());}});
          myTableArray.push(arrayOfThisRow);
      }
  });
  return myTableArray;
} // End makeArrayFromTable function.

// Function that make the post request to add customer.
function addCustomer(){
  if ($('#fullName').val().toString().trim() === ""){
    alert("Full name is required");
    return;
  }
  var myTableArray = makeArrayFromTable();
  var checkLength = myTableArray.some((e) => e.length != 2);
  console.log(checkLength);
  if (checkLength){
    alert("Complete all Tintas section inputs");
    return;
  }

  $.ajax({
    data:{
      fullName : $('#fullName').val(),
      mobilePhone : $('#mobilePhone').val(),
      tintas : myTableArray.toString()
    },
    type:'POST',
    url:'/customer/'
  })
  .done(function(data){
    (data.error) ? console.log(error) : window.location.href = '/customers/';
  });
} // End addCustomer function

// Function that make the put request to update customer.
function updateCustomer(id){
  if ($('#fullName').val().toString().trim() === ""){
    alert("Full name is required");
    return;
  }
  var myTableArray = makeArrayFromTable();
  var checkLength = myTableArray.some((e) => e.length != 2);
  console.log(checkLength);
  if (checkLength){
    alert("Complete all Tintas section inputs");
    return;
  }

  $.ajax({
    data:{
      fullName : $('#fullName').val(),
      mobilePhone : $('#mobilePhone').val(),
      tintas : myTableArray.toString()
    },
    type:'PUT',
    url:`/customer/${id}/`
  })
  .done(function(data){
    (data.error) ? console.log(error) : window.location.href = '/customers/';
  });
} // End updateCustomer function
