function verifemail(inputtxt)
      { 
      if(inputtxt.value.indexOf('@') > -1)
      {
      return true;
      }
      else
      {
      alert("Please enter an '@' symbol");
      return false;
      }
      }