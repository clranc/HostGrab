HostGrab
========
This is a tool meant for people who enjoy blocking ads with a host file but
find it tedious to have navigate to the one they like, download it, and then manually import it to their root directory. 

I made this as part of a personal project to teach myself python as well as how to use git.  So my code documentation 
doesn't meet up to python standards yet which I'm still working on.   

Useful Features 
------------------

 - Managing download links for various host files 
 - Storing IP and Domain exceptions you want to include in the host file you import. **ie:** setting facebook to point to your home address so you can focus on work
 - Scans hosts when downloaded to verify if there are any faulty or suspiciousIP addresses
 - If you're the kind of person who perfers a host file with an ungodly amount of ad domains to block (and as a result blocks websites you need to use) a swap feature is included that swaps your imported host file with a default one.  After which you can run the command again to load your host back in to continue blocking away.  


Commands
-----------
 - url 
   - add
   - rm
   - print
 - ipexc
   - add
   - rm
   - print
 - file
   - dl
   - import
   - scan
 - help
