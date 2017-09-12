

	for(i=1;i<=rows;i++)

	{

	  output = output + "<tr>";

	  while(j<=cols)

	  {

	     output = output + "<td>" + i*j + "</td>";

	     j = j+1;

	  }

	  output = output + "</tr>";

	  j = 1;

	}

