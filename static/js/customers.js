var customerIdToDelete = 0;
// Function that make the delete request to delete customer.
function deleteCustomer(){
  $.ajax({
    type:'DELETE',
    url:`/customer/${customerIdToDelete}/`
  })
  .done(function(data){
    (data.error) ? console.log(error) : window.location.href = '/customers/';
  });
} // End deleteCustomer function

function showModal(id, name){
  customerIdToDelete = id;
  $('#delteCustomerModalBody').text(`Are you sure you want to delete the customer ${name}?`);
  $('#deleteCustomerModal').modal('show');
}
