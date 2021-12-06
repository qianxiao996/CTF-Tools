function decode(source) {
    output = ''    
    if (source.length > 0) 
    {
        l = ''
        
        if (source.length > 3 && source.slice(source.length-3) == ')()')
        {
            //eval-ed
            s = source.slice(0, source.length - 2)
            i = s.length
          
            //first try----------------------------
            while (i--) {
                //if ((l = s.slice(i)).split(')').length == l.split('(').length) break
                l = s.slice(i)
                if (l.split(')').length == l.split('(').length) {
                    break;
                }
            }
            //-------------------------------------
        }
        else
        {
            l = source;
        }
            
        txtResult = eval(l)
        return txtResult

    }
}