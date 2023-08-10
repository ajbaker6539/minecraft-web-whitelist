function clicked(e, type)
{
    if(type=="reject") {
        if(!confirm('Are you sure you want to reject?')) {
            e.preventDefault();
        }
    }
    else if (type=="accept") {
        if(!confirm('Are you sure you want to accept?')) {
            e.preventDefault();
        }
    }
}