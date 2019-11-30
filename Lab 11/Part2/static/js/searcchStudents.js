function searchTable()
{
 var input, filter, table, tr, td, i, txtValue;
 input = document.getElementById("myInput");
 console.log(input);
 filter = input.value.toUpperCase();
 console.log(filter);
 table = document.getElementById('tables');
 console.log(table);
 tr = table.getElementsByTagName('tr');
 console.log(tr);

 for(i = 1; i < (tr.length-1); i++)
 {
     td = tr[i].getElementsByTagName('td')[0];
     if (td)
     {
         txtValue = td.innerHTML || td.textContent;
         if (txtValue.toUpperCase().indexOf(filter) > -1)
         {
             tr[i].style.display = '';
         }
         else
         {
             tr[i].style.display = 'none';
         }
     }
 }
}