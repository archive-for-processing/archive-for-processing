# Archive for Processing

Archive for Processing is an (unofficial) archive of resources for the Processing community.

It is intended to make the distributed ecosystem of open source libraries, modes, tools, example sets, and documentation a bit more robust.

This GitHub organization account does so by providing simple mirroring via a list of forked GitHub repositories. These forks help guard against future project loss, and in particular make availabile the work by former contributors who have moved on from the Processing community and no longer maintain their associated accounts, websites, et cetera.

This archive contains both inactive and active projects -- it includes forks of ongoing, under-development repositories. When viewing a repository in the archive, **FIRST CHECK THE SOURCE REPO** linked under the title, if that original source exists. The archival forks may be out-of-date, with an up-to-date version being developed by the original author or maintainer. Forks for active repositories do not automatically update -- they are snapshots that must be periodically refreshed.

The repository forks here are not maintained in any way, even if the original is no longer available. As such, they do not accept issues, comments, etc. They are available to fork for interested developers, including future volunteer maintainers.

This independent initiative is not an official project of the Processing Foundation.

## Scripts

This repository contains two main scripts:

1.  contirbutions/contrib_archive.py

    Downloads all PDE Contributions Manager listings: Libraries, Examples,
    Tools, and Modes -- including disabled, if available -- as txt listings
    and zip files.
    
    -  txt listings are archived in the 'data' branch, under contributions/txt
    -  zip files are not stored in this repository

2.  github_fork_updater.py

    Attempts to periodically keep the master branch of all forks on all repos
    up-to-date on GitHub, using the API and the following sequence:
    
    ```
    git clone repo_url
    git remote add upstream repo.source.clone_url
    git fetch upstream
    git checkout master
    git merge upstream/master
    git push
    ```

## Sources

The GitHub project account contains a large number of forked repos.
These are maintained through a github org account and its forks.
Some of these (and some resources which are not repos, or cannot be forked) are found below in a manually updated and sorted list. Repo forks are periodically brought up to date on their master branch with `github_fork_updater.py` 

Forks are only made of public repos. If accounts are removed, repos are deleted, or repos are taken private, the archive fork attempts to preserve that last public snapshot of the repo.

> https://help.github.com/en/articles/what-happens-to-forks-when-a-repository-is-deleted-or-changes-visibility
>
> **Deleting a public repository**  
> When you delete a public repository, one of the existing public forks is chosen to be the new parent repository. All other repositories are forked off of this new parent and subsequent pull requests go to this new parent.
> 
> **Changing a public repository to a private repository**  
> If a public repository is made private, its public forks are split off into a new network. As with deleting a public repository, one of the existing public forks is chosen to be the new parent repository and all other repositories are forked off of this new parent. Subsequent pull requests go to this new parent.

A key limitation is that the Processing Library Template has been forked by a number of projects.
Each of these projects counts as the "same repo," and thus only one of all of them can be forked by the Archive for Processing account.

A workaround might involve iterating over an "unforkable" url list and treating as a remote for a clean repo outside the API.


### libraries

Contributed libraries -- this means all libraries _except_ ones integrated into Processing / p5.js / PDE or hosted on the official processing foundation github account at https://github.com/processing/.

-  collected Java mode (and some Java-affiliated) listings on processing.org:
   -  [Libraries listed processing.org](https://processing.org/reference/libraries/) are forked if they link to an open source repository on github.
-  collected p5.js listings:
   -  https://github.com/ITPNYU/p5.ble.js
   -  https://github.com/sarahgp/p5bots
   -  https://github.com/Lartu/p5.clickable
   -  https://github.com/bmoren/p5.collide2D
   -  https://github.com/piratesjustar/p5.createLoop
   -  https://github.com/Smilebags/p5.dimensions.js
   -  https://github.com/loneboarder/p5.experience.js
   -  https://github.com/IDMNYU/p5.js-func
   -  https://github.com/bmoren/p5.geolocation
   -  https://github.com/charlieroberts/p5.gibber.js
   -  https://github.com/jagracar/grafica.js
   -  https://github.com/bitcraftlab/p5.gui
   -  https://github.com/cvalenzuela/Mappa
   -  https://github.com/bobcgausa/cook-js
   -  https://github.com/molleindustria/p5.play
   -  https://github.com/dhowe/RiTaJS
   -  https://github.com/mveteanu/p5.SceneManager
   -  https://github.com/generative-light/p5.scribble.js
   -  https://github.com/p5-serial/p5.serialport
   -  https://github.com/IDMNYU/p5.js-speech
   -  https://github.com/linux-man/p5.tiledmap
   -  https://github.com/Dozed12/p5.voronoi

-  Other (e.g. announced through forum posts):
   -  https://github.com/linux-man/VLCJVideo
   -  https://github.com/archive-for-processing/GameLibZero
   -  Johnny-Five for Processing p5.js https://github.com/monteslu/p5.j5
   -  https://github.com/PBernalPolo/RPiModules
   -  https://discourse.processing.org/t/networking-processing-client-to-php-server/12466


### now archived from non-github sources:
   -  triangulate

### unarchived libraries (javascript)

-  ASCII art https://www.tetoki.eu/asciiart/
-  p5.3D https://github.com/FreddieRa/p5.3D
-  vida https://www.tetoki.eu/vida/

### unarchived libraries (java)

-  Not available on github:
   -  Bitbucket
      -  toxiclibs https://bitbucket.org/postspectacular/toxiclibs/
      -  PControls https://forum.processing.org/two/discussion/454/processing-pcontrols https://bitbucket.org/fpercival/processing-pcontrols/downloads/
   -  gitorious
      -  http://www.ricardmarxer.com/fisica/
   -  Google Code
      -  AmbientLightSensor http://projects.formatlos.de/ambientlightsensor/
      -  ezgestures http://www.silentlycrashing.net/ezgestures/
      -  MindSet Processing http://jorgecardoso.eu/processing/MindSetProcessing/
      -  Mother http://www.onar3d.com/mother/
      -  NXTComm http://jorgecardoso.eu/processing/NXTComm/
      -  TimedEvents http://multiply.org/processing/ https://code.google.com/archive/p/processing-timed-events-library/
   -  SourceForge
      -  projms https://sourceforge.net/projects/projms/ https://www.graffitiresearchlab.de/projms/
-  Not found (self-hosted / private / unclear)
      -  AULib https://imaginary-institute.com/resources/AULibrary/AULibrary.php https://forum.processing.org/two/discussion/7745/au-library-released
      -  BlobDetection http://www.v3ga.net/processing/BlobDetection/
      -  correlations http://www.muehlseife.de/correlations-library/
      -  J4K (Java4Kinect) https://forum.processing.org/two/discussion/1497/j4k-java-for-kinect-library-is-now-released-for-processing-2
      -  GaussSense SDK http://developers.gausstoys.com/ https://github.com/gausstoys
      -  ID3 http://jorgecardoso.eu/processing/ID3/
      -  ImageP ImageJ for Processing https://forum.processing.org/two/discussion/2924/porting-imagej-to-processing-a-first-class-videowriter
      -  File search class https://forum.processing.org/two/discussion/6878/file-search-class
      -  MapThing http://www.reades.com/MapThing/
      -  network graph visualizer https://forum.processing.org/two/discussion/7765/network-graph-visualizer-announcement
      -  Papaya a.com/papayastatistics/ -- must be built from source? https://discourse.processing.org/t/can-someone-try-to-find-this-library-in-processing/1488/11 -- older mirror here: https://github.com/kfrajer/papaya
      -  PixelPusher http://www.heroicrobotics.com/
      -  P8gGraphicsSVG http://phi.lho.free.fr/programming/Processing/P8gGraphicsSVG/
      -  quark / Peter Lager libraries, all: http://www.lagers.org.uk/
         -  AI for Games http://www.lagers.org.uk/ai4g/index.html
         -  G4P (GUI for processing) http://www.lagers.org.uk/g4p/index.html
         -  Game Control Plus http://www.lagers.org.uk/gamecontrol/index.html
         -  Jasmine http://www.lagers.org.uk/jasmine/
         -  Path Finder http://www.lagers.org.uk/pfind/index.html
         -  QScript http://www.lagers.org.uk/qscript/
         -  Shapes3D http://www.lagers.org.uk/s3d4p/index.html
         -  Sprites http://www.lagers.org.uk/s4p/index.html
         -  Steganos http://www.lagers.org.uk/steganos/index.html
      -  SuperCollider client for Processing http://www.erase.net/projects/processing-sc/
      -  temboo https://temboo.com/processing
      -  toloop https://discourse.processing.org/t/tooloop-open-media-server/1680
      -  Traer Physics 3.0 http://murderandcreate.com/physics/
      -  ttslib https://www.local-guru.net/blog/pages/ttslib
      -  UDP http://ubaa.net/shared/processing/udp/
-  Broken links:
   -  See listed problems on issue: https://github.com/processing/processing-docs/issues/760
   -  GML4U https://github.com/01010101/GML4U/wiki
     -  ... although did fork https://github.com/joshuajnoble/GML4U
   -  SFTP for Processing https://shiffman.net/2007/06/04/sftp-with-java-processing/
   -  Tablet by Andres Colubri http://interfaze.info/libraries/tablet/
   -  Eliza by Andres Colubri http://interfaze.info/libraries/eliza/
   -  https://github.com/danieljayB/jpcapSniffer https://forum.processing.org/two/discussion/6408/processing-library-construction-help-feedback
   -  https://forum.processing.org/two/discussion/6815/lemmingsscanner-release
   -  KinematikJava http://labaaa.org/kinematikjava/ https://forum.processing.org/two/discussion/10245/library-for-kinematics-of-6-axis-robot

-  Unforkable:  
   Some Processing libraries are forks of the Processing Library Template. Due to a limitation in GitHub, they cannot be forked by the same account (libraries that cannot be forked due to shared ancestor limitations).
   -  colourlovers https://forum.processing.org/two/discussion/2736/new-library-that-integrates-processing-with-colourlovers-com https://github.com/triss/colourlovers
   -  grafica (java version) https://github.com/jagracar/grafica/tree/master/src/grafica
   -  HersheyFont https://github.com/ixd-hof/HersheyFont https://forum.processing.org/two/discussion/9520/hershey-line-font-library
   -  HPGLGraphics https://github.com/ciaron/HPGLGraphics
   -  keystoned https://github.com/clankill3r/keystoned/ (update described in https://forum.processing.org/two/discussion/4338/keystoned-update-on-david-bouchard-keystone-library)
   -  mbedJS-Processing-API https://github.com/nyatla/mbedJS-Processing-API https://forum.processing.org/two/discussion/6466/processing-mbed-over-websocket
   -  NextText https://github.com/prisonerjohn/NextText
   -  picking https://github.com/nclavaud/picking
   -  processing-countdowntimer https://github.com/dhchoi/processing-countdowntimer
   -  proscene https://github.com/remixlab/proscene
   -  RiftIt (Occulus Rift) https://github.com/pion3er/RiftIt https://forum.processing.org/two/discussion/2223/riftit-oculus-rift-for-processing
   -  SeeneLib https://forum.processing.org/two/discussion/935/unofficial-seene-library https://github.com/BenVanCitters/SeeneLib---Processing-Library
   -  vsync https://github.com/erniejunior/VSync-for-Processing
   -  wooting keyboard https://github.com/Shinhoo/Wooting-Keyboard-Library


## modes and related systems

-  JRubyArt https://github.com/ruby-processing/JRubyArt
-  p5.js https://github.com/processing/p5.js
-  p5py https://github.com/p5py/p5
-  Processing.py https://github.com/jdf/processing.py
-  Processing for Android https://github.com/archive-for-processing/processing-android
-  Processing.R https://github.com/archive-for-processing/Processing.R

## other

-  APDE (Android) https://github.com/archive-for-processing/APDE
-  TweakMode https://github.com/archive-for-processing/TweakMode

## to survey

-  gicentre https://www.gicentre.net/software/
-  forum two:
   -  https://forum.processing.org/two/categories/create-announce-libraries
      -  pgs 5-8: complete
         - [x] BlobScanner https://github.com/robdanet/blobscanner https://forum.processing.org/two/discussion/2518/blobscanner-new-release-v-0-1-alpha
         - [x] colorlib https://github.com/vormplus/colorLib https://forum.processing.org/two/discussion/10054/colorlib-2-0-0-for-processing-2
         - [x] L3D https://github.com/enjrolas/L3D-Library https://forum.processing.org/two/discussion/8325/led-cube-library-for-processing
         - [x] OpenDMX https://github.com/orcaomar/processing-opendmx https://forum.processing.org/two/discussion/5444/direct-opendmx-hardware-control-from-processing-for-windows-only
         - [x] PSR Processing Recorder Library https://github.com/tomasgvivo/PSR https://forum.processing.org/two/discussion/6110/processing-recorder-library
         - [x] Processinglue https://github.com/yasutonakanishi/Processinglue
         - [x] PatchMatch https://github.com/davidchatting/PatchMatch
         - [x] SurfaceLib https://github.com/eskimoblood/surfacelib https://forum.processing.org/two/discussion/4112/porting-surfacelib-to-processing-2
         - [x] VMap (SurfaceMapper for Processing 2) https://github.com/AlanChatham/VMap https://forum.processing.org/two/discussion/7635/surfacemapper-fork-for-processing-2
         - [x] blob-tracker https://github.com/pschaeffer/blob-tracker https://forum.processing.org/two/discussion/10117/new-processing-libraries
         - [x] color-palette https://github.com/pschaeffer/color-palette https://forum.processing.org/two/discussion/10117/new-processing-libraries
      -  pgs 1-4:
         - ... not yet collected
   -  https://forum.processing.org/two/categories/create-announce-modes
   -  https://forum.processing.org/two/categories/create-announce-tools

### general purpose Java resources (not Processing-specific)

-  https://math.nist.gov/javanumerics/jama/

   
