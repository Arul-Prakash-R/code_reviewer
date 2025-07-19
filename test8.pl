#!/usr/bin/perl
use CGI;

my $q = CGI->new;
my $host = $q->param('host'); # ?host=127.0.0.1;ls
print "Content-type: text/plain\n\n";
print `ping -c 1 $host`;
    