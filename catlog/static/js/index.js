// alert('hello world')

// const input = document.querySelector('input');
// const log = document.getElementById('account_kit');
//
// input.addEventListener('change', updateValue);
//
// function updateValue(e) {
//
//   alert('Hello welcome kit')
// }

window.onload = () => {
  document.getElementById("myBtn").disabled = true;
}
function set_parameter(data){
  if (data['data'] == 'False'){
    console.log(data,'Data')
    cust=document.getElementById('account_kit').style.border='3px solid #A02905';
    document.getElementById('cust_id').innerHTML='Invalid Welcome Kit Number'+'&#10060;'
    document.getElementById('cust_id').style.color='red'
    document.getElementById("myBtn").disabled = true;
    document.getElementById('debit_kit').disabled=true;
  }
  else{
    console.log(data,'Data True')
    cust=document.getElementById('account_kit').style.border='3px solid #99FF99';
    document.getElementById('cust_id').innerHTML='Valid Welcome Kit Number'+'&#9989;'
    document.getElementById('cust_id').style.color='#60CE80'
    // document.getElementById("myBtn").disabled = false;
    document.getElementById('debit_kit').disabled=false;
  }


}

function set_parameter_debit(data){
  if (data['data'] == 'False'){
    console.log(data,'Data')
    cust=document.getElementById('debit_kit').style.border='3px solid #A02905';
    document.getElementById('debit_id').innerHTML='Invalid Debit Kit Number'+'&#10060;'
    document.getElementById('debit_id').style.color='red'
    document.getElementById("myBtn").disabled = true;
  }
  else{
    console.log(data,'Data True')
    cust=document.getElementById('debit_kit').style.border='3px solid #99FF99';
    document.getElementById('debit_id').innerHTML='Valid Debit Kit Number'+'&#9989;'
    document.getElementById('debit_id').style.color='#60CE80'
    document.getElementById("myBtn").disabled = false;
  }


}




function load_bar(x)
{
    if (x==0)
    {
    $(document.body).css( {"cursor": "default"} );
    $("body").css( {"cursor": "wait"} );
    $("body").css("visibility", "hidden"); //modal window
//  $("#doc").....ENABLE all clicks (left/right/etc)
    }

    else if (x==1)
    {
    $(document.body).css( {"cursor": "wait"} );
    $("body").css( {"cursor": "default"} );
    $("body").css( {"visibility": "visible"} ); //modal window
//  $("#doc").....DISABLE all clicks (left/right/etc)
    }

    else
    {
    return alert("Wrong argument!");
    }
}

function welcomeKitValidate(value){
  url='/validate/?value='+value
  // load_bar(0)
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const data= JSON.parse(xhttp.responseText)
        console.log(xhttp.responseText,data);
        console.log(typeof(xhttp.responseText));
        // console.log(data)
          set_parameter(data)

        // load_bar(1)

      }
    };
    xhttp.open("GET", url, true);
    xhttp.send();

}



function debitValidate(value){
  url='/validate/?value='+value
  // load_bar(0)
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const data= JSON.parse(xhttp.responseText)
        console.log(xhttp.responseText,data);
        console.log(typeof(xhttp.responseText));
        // console.log(data)
          set_parameter_debit(data)

        // load_bar(1)

      }
    };
    xhttp.open("GET", url, true);
    xhttp.send();

}
