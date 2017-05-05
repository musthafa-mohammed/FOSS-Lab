#/user/bin/perl -w
$var = "The cat ate all the food";
#Modifing each occurence of cat with dog using s///
$var =~ s/cat/dog/;
print "The modified string is $var\n";
#Changing the whole sentence into Uppercase  using tr///

$var =~ tr/a-z/A-Z/;
print "The capitalized string is $var\n";
