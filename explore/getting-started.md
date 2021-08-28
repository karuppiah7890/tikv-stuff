I was just reading through the https://tikv.org website's landing page

It talks about "raw" key-value API and ACID-compliant key-value API. I'll have to go and check what they mean by raw key-value API [TODO]

Apparently it's used as a storage system in use cases like
- the metadata storage system for object storage service
- the storage system for recommendation systems
- the online feature store - https://www.featurestore.org/

I'm not sure what the https://www.featurestore.org/ is, sounds cool, ML and stuff. I'll check it out sometime [TODO]

Also, looks like TiKV is used in many projects. They list out

TiKV is also widely used as the storage layer for database management systems, for example:

- TiDB: An open-source MySQL compatible NewSQL database that supports Hybrid Transactional and Analytical Processing (HTAP) workloads.
- Zetta: An open-source NoSQL database that supports Transaction and Cloud Spanner like API.
- Tidis: a Distributed NoSQL database, providing a Redis protocol API (string, list, hash, set, sorted set), written in Go.
- Titan: A distributed implementation of Redis compatible layer based on TiKV.
- JuiceFS: An open-source POSIX file system that is based on TiKV and S3.

https://github.com/pingcap/tidb

https://github.com/zhihu/zetta

https://github.com/yongman/tidis

https://github.com/distributedio/titan

https://github.com/juicedata/juicefs

It's interesting to see Redis API like layer on top of TiKV in Tidis and Titan. And of course interesting to see MySQL API layer on top of TiKV. I have heard of TiDB before from an ex-colleague, that's how I first heard about TiDB and TiKV. My colleague was even contributing to one of those projects. He mentioned that these were interesting projects but I hadn't peeked into them at the time!

I'm also wondering what the "NewSQL" means, something to checkout [TODO], but it's interesting to see HTAP. My colleague used to talk about OLAP - Online Analytical Processing and OLTP - Online Transactional Processing. Here it talks about a hybrid - both Transactional and Analytical. So it's interesting! I need to read more about OLAP, OLTP and HTAP. I remember checking them out during college days when I couldn't care less about databases those days 🙈

Interesting to see mention of Cloud Spanner. I have heard it to be a very popular product in Google. I have also heard about the research paper but haven't read it

I wonder what JuiceFS does with TiKV. I'm assuming it stores metadata about the files stored in S3, this is probably the use case mentioned in the "the metadata storage system for object storage service", where S3 is the object storage service. Sounds like it!

AND TiKV is written in rust ;)

https://github.com/tikv/tikv

---

There's an interesting list of mentions around "Why TiKV?" I see mention of low and stable latency / response time. I wonder what's "stable" about latency, gotta check [TODO]. I'm guessing / assuming it's something to do with having the same latency almost always and that too a very low latency in this case, which is very idea. I can see 1ms being mentioned as response time and mention of 99th percentile value of 10ms, meaning 99% of requests have response times less than or equal to 10ms. Interesting! I remember Redis conf 2021 talking about how they are aiming for such latencies too!

Looks like TiKV can scale a lot, like, terabytes. I do remember some people showing off and talking about managing petabytes for some of their systems.

And also easy to maintain. Wow. That's like the usual "dream come true" for operators, developers and everyone. It seems to use some sort of operator / package manager. TiUP is a package manager it seems

https://tikv.org/docs/5.1/reference/tiup/

https://docs.pingcap.com/tidb/stable/tiup-documentation-guide

I just skimmed through https://docs.pingcap.com/tidb/stable/tiup-overview and it seems to be pretty interesting! A package manager to manage the components. But the page mentions that the components are components in the TiDB ecosystem. I'm wondering if TiKV is part of it or not. I mean, I think it is part of it, as TiDB depends on TiKV. I'll know once I install TiKV through quick start / getting started. I do see playground commands in TiUP

Now, back to TiKV stuff. Apparently TiKV's design is based on Google Spanner and HBase but it's easier to maintain without dependency on any distributed file system it seems. I wonder what that means. Are they talking about some system like Hadoop Distributed File System, hmm. Not sure, only reading Google Spanner and HBase research papers can help. Gotta read them [TODO]

https://research.google/pubs/pub39966/

https://hbase.apache.org/

It also talks about "consistent distributed transactions" which I need to read about first [TODO] and says "Similar to Google’s Spanner, TiKV (TxnKV mode) supports externally consistent distributed transactions." I wonder what "externally consistent distributed transactions" means. [TODO]

And it also says "In RawKV and TxnKV modes, you can customize the balance between consistency and performance." I wonder what that means, is it related to CAP theorem? 🤔 But that would be consistency and availability, here it says performance, related? Gotta check [TODO]

I can see a lot of adopters too, with case studies!

https://tikv.org/adopters/

---

Let's check getting started from the main page top link

https://tikv.org/docs/5.1/concepts/overview/

There is another link too, for 5 mins quick start https://tikv.org/docs/5.1/concepts/tikv-in-5-minutes/ but I think I'll do a small reading of some stuff first :)

Reading https://tikv.org/docs/5.1/concepts/overview/ , it says

"TiKV is intended to fill the role of a unified distributed storage layer. TiKV excels at working with large-scale data by supporting petabyte-scale deployments spanning trillions of rows."

It can do petabytes too ;) I need to understand more about "unified distributed storage layer". I'm guessing what it means is - if I want to implement a database, I can worry about client communication, query parsing and execution and finally store stuff to disk using TiKV? I don't know, seems like it. Gotta check [TODO]

https://tikv.org/img/basic-architecture.png

I'm gonna try the 5 minutes trial and then checkout this https://tikv.org/docs/5.1/reference/architecture/overview/ next

https://tikv.org/docs/5.1/concepts/tikv-in-5-minutes/

For production, we gotta check https://tikv.org/docs/5.1/deploy/install/install/ it seems. I'll check that too soon [TODO]

```bash
tikv-stuff $ curl --proto '=https' --tlsv1.2 -sSf https://tiup-mirrors.pingcap.com/install.sh | sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 6825k  100 6825k    0     0  2337k      0  0:00:02  0:00:02 --:--:-- 2336k
WARN: adding root certificate via internet: https://tiup-mirrors.pingcap.com/root.json
You can revoke this by remove /Users/karuppiahn/.tiup/bin/7b8e153f2e2d0928.root.json
Successfully set mirror to https://tiup-mirrors.pingcap.com
Detected shell: bash
Shell profile:  /Users/karuppiahn/.bash_profile
/Users/karuppiahn/.bash_profile has been modified to add tiup to PATH
open a new terminal or source /Users/karuppiahn/.bash_profile to use it
Installed path: /Users/karuppiahn/.tiup/bin/tiup
===============================================
Have a try:     tiup playground
===============================================
tikv-stuff $ tail -n 5 ~/.bash_profile 
export GPG_TTY=$(tty)

export PS1="\W \$ "

export PATH=/Users/karuppiahn/.tiup/bin:$PATH
tikv-stuff $ source .bash_profile
-bash: .bash_profile: No such file or directory
tikv-stuff $ source ~/.bash_profile
tikv-stuff $ ti
tic                 tiff2pdf            tiffdither          tifftopnm           timerfires
tidy                tiff2ps             tiffdump            tiffutil            times
tidy_changelog      tiff2rgba           tiffinfo            tig                 timesyncanalyse
tidy_changelog5.30  tiffcmp             tiffmedian          tilt                tiup
tiff2bw             tiffcp              tiffset             time                
tiff2icns           tiffcrop            tiffsplit           timer_analyser.d    
tikv-stuff $ tiup 
TiUP is a command-line component management tool that can help to download and install
TiDB platform components to the local system. You can run a specific version of a component via
"tiup <component>[:version]". If no version number is specified, the latest version installed
locally will be used. If the specified component does not have any version installed locally,
the latest stable version will be downloaded from the repository.

Usage:
  tiup [flags] <command> [args...]
  tiup [flags] <component> [args...]

Available Commands:
  install     Install a specific version of a component
  list        List the available TiDB components or versions
  uninstall   Uninstall components or versions of a component
  update      Update tiup components to the latest version
  status      List the status of instantiated components
  clean       Clean the data of instantiated components
  mirror      Manage a repository mirror for TiUP components
  telemetry   Controls things about telemetry
  completion  Output shell completion code for the specified shell (bash or zsh)
  env         Show the list of system environment variable that related to TiUP
  help        Help about any command or component

Components Manifest:
  use "tiup list" to fetch the latest components manifest

Flags:
  -B, --binary <component>[:version]   Print binary path of a specific version of a component <component>[:version]
                                       and the latest version installed will be selected if no version specified
      --binpath string                 Specify the binary path of component instance
      --help                           Help for this command
      --skip-version-check             Skip the strict version check, by default a version must be a valid SemVer string
  -T, --tag string                     Specify a tag for component instance
  -v, --version                        Print the version of tiup

Component instances with the same "tag" will share a data directory ($TIUP_HOME/data/$tag):
  $ tiup --tag mycluster playground

Examples:
  $ tiup playground                    # Quick start
  $ tiup playground nightly            # Start a playground with the latest nightly version
  $ tiup install <component>[:version] # Install a component of specific version
  $ tiup update --all                  # Update all installed components to the latest version
  $ tiup update --nightly              # Update all installed components to the nightly version
  $ tiup update --self                 # Update the "tiup" to the latest version
  $ tiup list                          # Fetch the latest supported components list
  $ tiup status                        # Display all running/terminated instances
  $ tiup clean <name>                  # Clean the data of running/terminated instance (Kill process if it's running)
  $ tiup clean --all                   # Clean the data of all running/terminated instances

Use "tiup [command] --help" for more information about a command.
tikv-stuff $ 
tikv-stuff $ tiup version
The component `version` version  is not installed; downloading from repository.
^C
tikv-stuff $ tiup --version
1.5.5 tiup
Go Version: go1.16.7
Git Ref: v1.5.5
GitHash: 01df6de49dbf23af1a3e9d6f71d383c407cdb810
tikv-stuff $ tiup update --self
download https://tiup-mirrors.pingcap.com/tiup-v1.5.5-darwin-amd64.tar.gz 6.67 MiB / 6.67 MiB 100.00% 4.40 MiB/s     
Updated successfully!
tikv-stuff $ tiup update --self
download https://tiup-mirrors.pingcap.com/tiup-v1.5.5-darwin-amd64.tar.gz 6.67 MiB / 6.67 MiB 100.00% 3.97 MiB/s     
Updated successfully!
tikv-stuff $ tiup update playground

download https://tiup-mirrors.pingcap.com/playground-v1.5.5-darwin-amd64.tar.gz 203.48 KiB / 7.29 MiB 2.73% 336.68 Kidownload https://tiup-mirrors.pingcap.com/playground-v1.5.5-darwin-amd64.tar.gz 424.48 KiB / 7.29 MiB 5.69% 336.68 Kidownload https://tiup-mirrors.pingcap.com/playground-v1.5.5-darwin-amd64.tar.gz 866.48 KiB / 7.29 MiB 11.61% 336.68 Kdownload https://tiup-mirrors.pingcap.com/playground-v1.5.5-darwin-amd64.tar.gz 1.71 MiB / 7.29 MiB 23.45% 481.32 KiBdownload https://tiup-mirrors.pingcap.com/playground-v1.5.5-darwin-amd64.tar.gz 3.44 MiB / 7.29 MiB 47.12% 481.32 KiBdownload https://tiup-mirrors.pingcap.com/playground-v1.5.5-darwin-amd64.tar.gz 5.28 MiB / 7.29 MiB 72.49% 481.32 KiBdownload https://tiup-mirrors.pingcap.com/playground-v1.5.5-darwin-amd64.tar.gz 7.29 MiB / 7.29 MiB 100.00% 3.97 MiB/s
Updated successfully!
tikv-stuff $ 
tikv-stuff $ tiup -v
1.5.5 tiup
Go Version: go1.16.7
Git Ref: v1.5.5
GitHash: 01df6de49dbf23af1a3e9d6f71d383c407cdb810
tikv-stuff $ tiup playground --mode tikv-slim
Starting component `playground`: /Users/karuppiahn/.tiup/components/playground/v1.5.5/tiup-playground --mode tikv-slim
Using the version v5.2.0 for version constraint "".

If you\'d like to use a TiDB version other than v5.2.0, cancel and retry with the following arguments:
    Specify version manually:   tiup playground <version>
    Specify version range:      tiup playground ^5
    The nightly version:        tiup playground nightly

Playground Bootstrapping...
The component `prometheus` version v5.2.0 is not installed; downloading from repository.
download https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 951.48 KiB / 39.78 MiB 2.34% 1.47 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 5.89 MiB / 39.78 MiB 14.81% 1.91 MiB/download https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 8.02 MiB / 39.78 MiB 20.17% 1.91 MiB/download https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 10.31 MiB / 39.78 MiB 25.93% 1.91 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 12.48 MiB / 39.78 MiB 31.38% 2.49 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 14.56 MiB / 39.78 MiB 36.59% 2.49 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 16.71 MiB / 39.78 MiB 42.01% 2.49 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 18.94 MiB / 39.78 MiB 47.61% 3.02 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 21.10 MiB / 39.78 MiB 53.03% 3.02 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 23.20 MiB / 39.78 MiB 58.31% 3.02 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 25.42 MiB / 39.78 MiB 63.91% 3.53 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 27.70 MiB / 39.78 MiB 69.64% 3.53 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 29.86 MiB / 39.78 MiB 75.06% 3.53 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 32.10 MiB / 39.78 MiB 80.68% 4.02 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 34.16 MiB / 39.78 MiB 85.86% 4.02 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 36.42 MiB / 39.78 MiB 91.54% 4.02 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 38.59 MiB / 39.78 MiB 97.00% 4.46 MiBdownload https://tiup-mirrors.pingcap.com/prometheus-v5.2.0-darwin-amd64.tar.gz 39.78 MiB / 39.78 MiB 100.00% 9.24 MiB/s
download https://tiup-mirrors.pingcap.com/grafana-v5.2.0-darwin-amd64.tar.gz 205.48 KiB / 47.12 MiB 0.43% 340.00 KiB/download https://tiup-mirrors.pingcap.com/grafana-v5.2.0-darwin-amd64.tar.gz 426.48 KiB / 47.12 MiB 0.88% 340.00 KiB/download https://tiup-mirrors.pingcap.com/grafana-v5.2.0-darwin-amd64.tar.gz 668.11 KiB / 47.12 MiB 1.38% 340.00 KiB/download https://tiup-mirrors.pingcap.com/grafana-v5.2.0-darwin-amd64.tar.gz 944.48 KiB / 47.12 MiB 1.96% 397.53 KiB/download https://tiup-mirrors.pingcap.com/grafana-v5.2.0-darwin-amd64.tar.gz 47.12 MiB / 47.12 MiB 100.00% 6.32 MiB/s
Start pd instance
The component `pd` version v5.2.0 is not installed; downloading from repository.
download https://tiup-mirrors.pingcap.com/pd-v5.2.0-darwin-amd64.tar.gz 40.53 MiB / 40.53 MiB 100.00% 8.69 MiB/s     
Start tikv instance
The component `tikv` version v5.2.0 is not installed; downloading from repository.
download https://tiup-mirrors.pingcap.com/tikv-v5.2.0-darwin-amd64.tar.gz 19.21 MiB / 19.21 MiB 100.00% 7.98 MiB/s   
PD client endpoints: [127.0.0.1:2379]
To view the Prometheus: http://127.0.0.1:9090
To view the Grafana: http://127.0.0.1:3000

 
^CPlayground receive signal:  interrupt
Wait tikv(91361) to quit...
Got signal interrupt (Component: playground ; PID: 91336)
Grafana quit
prometheus quit
pd quit

tikv quit
Wait pd(91360) to quit...
tikv-stuff $ 
tikv-stuff $ tiup clean -h
Clean the data of instantiated components

Usage:
  tiup clean <name> [flags]

Flags:
      --all   Clean all data of instantiated components

Global Flags:
      --help                 Help for this command
      --skip-version-check   Skip the strict version check, by default a version must be a valid SemVer string
tikv-stuff $ tiup clean -all
Error: unknown shorthand flag: 'a' in -all
tikv-stuff $ tiup clean --all
tikv-stuff $ 
```

What's `--mode tikv-slim`?

https://docs.pingcap.com/tidb/stable/tiup-playground

I can't find `--mode` here too, hmm

```bash
tikv-stuff $ curl -o tikv-client-java.jar https://download.pingcap.org/tikv-client-java-3.2.0-SNAPSHOT.jar && \
> curl -o slf4j-api.jar https://repo1.maven.org/maven2/org/slf4j/slf4j-api/1.7.16/slf4j-api-1.7.16.jar
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100   243    0   243    0     0    176      0 --:--:--  0:00:01 --:--:--   176
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 40509  100 40509    0     0  44417      0 --:--:-- --:--:-- --:--:-- 44369
tikv-stuff $ 
tikv-stuff $ jshell
The operation couldn’t be completed. Unable to locate a Java Runtime.
Please visit http://www.java.com for information on installing Java.
```

Now I need to install Java, for `jshell`, hmm

https://github.com/shyiko/jabba

```bash
tikv-stuff $ curl -sL https://github.com/shyiko/jabba/raw/master/install.sh | bash && . ~/.jabba/jabba.sh

Installing v0.11.2...

Adding source string to /Users/karuppiahn/.bashrc
Adding source string to /Users/karuppiahn/.bash_profile
Adding source string to /Users/karuppiahn/.zshrc

Installation completed
(if you have any problems please report them at https://github.com/shyiko/jabba/issues)

tikv-stuff $ jabba ls-remote | less
tikv-stuff $ jabba ls-remote | less
tikv-stuff $ jabba install openjdk@1.16.0-1
Downloading openjdk@1.16.0-1 (https://download.java.net/java/GA/jdk16.0.1/7147401fd7354114ac51ef3e1328291f/9/GPL/openjdk-16.0.1_osx-x64_bin.tar.gz) 
181628041/181628041
Extracting /var/folders/4z/09jpfvfj6c19lxl7ch78pzvc0000gn/T/jabba-d-310700970 to /Users/karuppiahn/.jabba/jdk/openjdk@1.16.0-1 
tikv-stuff $ java
Usage: java [options] <mainclass> [args...]
           (to execute a class)
   or  java [options] -jar <jarfile> [args...]
           (to execute a jar file)
   or  java [options] -m <module>[/<mainclass>] [args...]
       java [options] --module <module>[/<mainclass>] [args...]
           (to execute the main class in a module)
   or  java [options] <sourcefile> [args]
           (to execute a single source-file program)

 Arguments following the main class, source file, -jar <jarfile>,
 -m or --module <module>/<mainclass> are passed as the arguments to
 main class.

 where options include:

    -cp <class search path of directories and zip/jar files>
    -classpath <class search path of directories and zip/jar files>
    --class-path <class search path of directories and zip/jar files>
                  A : separated list of directories, JAR archives,
                  and ZIP archives to search for class files.
    -p <module path>
    --module-path <module path>...
                  A : separated list of directories, each directory
                  is a directory of modules.
    --upgrade-module-path <module path>...
                  A : separated list of directories, each directory
                  is a directory of modules that replace upgradeable
                  modules in the runtime image
    --add-modules <module name>[,<module name>...]
                  root modules to resolve in addition to the initial module.
                  <module name> can also be ALL-DEFAULT, ALL-SYSTEM,
                  ALL-MODULE-PATH.
    --list-modules
                  list observable modules and exit
    -d <module name>
    --describe-module <module name>
                  describe a module and exit
    --dry-run     create VM and load main class but do not execute main method.
                  The --dry-run option may be useful for validating the
                  command-line options such as the module system configuration.
    --validate-modules
                  validate all modules and exit
                  The --validate-modules option may be useful for finding
                  conflicts and other errors with modules on the module path.
    -D<name>=<value>
                  set a system property
    -verbose:[class|module|gc|jni]
                  enable verbose output for the given subsystem
    -version      print product version to the error stream and exit
    --version     print product version to the output stream and exit
    -showversion  print product version to the error stream and continue
    --show-version
                  print product version to the output stream and continue
    --show-module-resolution
                  show module resolution output during startup
    -? -h -help
                  print this help message to the error stream
    --help        print this help message to the output stream
    -X            print help on extra options to the error stream
    --help-extra  print help on extra options to the output stream
    -ea[:<packagename>...|:<classname>]
    -enableassertions[:<packagename>...|:<classname>]
                  enable assertions with specified granularity
    -da[:<packagename>...|:<classname>]
    -disableassertions[:<packagename>...|:<classname>]
                  disable assertions with specified granularity
    -esa | -enablesystemassertions
                  enable system assertions
    -dsa | -disablesystemassertions
                  disable system assertions
    -agentlib:<libname>[=<options>]
                  load native agent library <libname>, e.g. -agentlib:jdwp
                  see also -agentlib:jdwp=help
    -agentpath:<pathname>[=<options>]
                  load native agent library by full pathname
    -javaagent:<jarpath>[=<options>]
                  load Java programming language agent, see java.lang.instrument
    -splash:<imagepath>
                  show splash screen with specified image
                  HiDPI scaled images are automatically supported and used
                  if available. The unscaled image filename, e.g. image.ext,
                  should always be passed as the argument to the -splash option.
                  The most appropriate scaled image provided will be picked up
                  automatically.
                  See the SplashScreen API documentation for more information
    @argument files
                  one or more argument files containing options
    -disable-@files
                  prevent further argument file expansion
    --enable-preview
                  allow classes to depend on preview features of this release
To specify an argument for a long option, you can use --<name>=<value> or
--<name> <value>.

tikv-stuff $ java -version
openjdk version "16.0.1" 2021-04-20
OpenJDK Runtime Environment (build 16.0.1+9-24)
OpenJDK 64-Bit Server VM (build 16.0.1+9-24, mixed mode, sharing)
    
tikv-stuff $ jshell 
|  Welcome to JShell -- Version 16.0.1
|  For an introduction type: /help intro

jshell> 
^C
tikv-stuff $
```

```bash
tikv-stuff $ jshell --class-path tikv-client-java.jar:slf4j-api.jar --startup test_raw.java

error: error reading tikv-client-java.jar; zip END header not found
error: error reading tikv-client-java.jar; zip END header not found
Exception in thread "main" java.lang.InternalError: Exception during analyze - java.lang.NullPointerException: Cannot invoke "com.sun.tools.javac.code.Scope$StarImportScope.isFilled()" because "tree.starImportScope" is null
	at jdk.jshell/jdk.jshell.TaskFactory$AnalyzeTask.analyze(TaskFactory.java:392)
	at jdk.jshell/jdk.jshell.TaskFactory$AnalyzeTask.<init>(TaskFactory.java:383)
	at jdk.jshell/jdk.jshell.TaskFactory.lambda$analyze$1(TaskFactory.java:178)
	at jdk.jshell/jdk.jshell.TaskFactory.lambda$runTask$4(TaskFactory.java:213)
	at jdk.compiler/com.sun.tools.javac.api.JavacTaskPool.getTask(JavacTaskPool.java:192)
	at jdk.jshell/jdk.jshell.TaskFactory.runTask(TaskFactory.java:206)
	at jdk.jshell/jdk.jshell.TaskFactory.analyze(TaskFactory.java:175)
	at jdk.jshell/jdk.jshell.TaskFactory.analyze(TaskFactory.java:161)
	at jdk.jshell/jdk.jshell.Eval.compileAndLoad(Eval.java:1034)
	at jdk.jshell/jdk.jshell.Eval.declare(Eval.java:914)
	at jdk.jshell/jdk.jshell.Eval.eval(Eval.java:139)
	at jdk.jshell/jdk.jshell.JShell.eval(JShell.java:493)
	at jdk.jshell/jdk.internal.jshell.tool.JShellTool.processSource(JShellTool.java:3609)
	at jdk.jshell/jdk.internal.jshell.tool.JShellTool.processSourceCatchingReset(JShellTool.java:1330)
	at jdk.jshell/jdk.internal.jshell.tool.JShellTool.processInput(JShellTool.java:1228)
	at jdk.jshell/jdk.internal.jshell.tool.JShellTool.run(JShellTool.java:1201)
	at jdk.jshell/jdk.internal.jshell.tool.JShellTool.startUpRun(JShellTool.java:1168)
	at jdk.jshell/jdk.internal.jshell.tool.JShellTool.resetState(JShellTool.java:1115)
	at jdk.jshell/jdk.internal.jshell.tool.JShellTool.start(JShellTool.java:941)
	at jdk.jshell/jdk.internal.jshell.tool.JShellToolBuilder.start(JShellToolBuilder.java:254)
	at jdk.jshell/jdk.internal.jshell.tool.JShellToolProvider.main(JShellToolProvider.java:120)
Caused by: java.lang.IllegalStateException: java.lang.NullPointerException: Cannot invoke "com.sun.tools.javac.code.Scope$StarImportScope.isFilled()" because "tree.starImportScope" is null
	at jdk.compiler/com.sun.tools.javac.api.JavacTaskImpl.analyze(JavacTaskImpl.java:383)
	at jdk.jshell/jdk.jshell.TaskFactory$AnalyzeTask.analyze(TaskFactory.java:389)
	... 20 more
Caused by: java.lang.NullPointerException: Cannot invoke "com.sun.tools.javac.code.Scope$StarImportScope.isFilled()" because "tree.starImportScope" is null
	at jdk.compiler/com.sun.tools.javac.comp.TypeEnter.ensureImportsChecked(TypeEnter.java:170)
	at jdk.compiler/com.sun.tools.javac.comp.Enter.complete(Enter.java:601)
	at jdk.compiler/com.sun.tools.javac.comp.Enter.main(Enter.java:561)
	at jdk.compiler/com.sun.tools.javac.main.JavaCompiler.enterTrees(JavaCompiler.java:1069)
	at jdk.compiler/com.sun.tools.javac.api.JavacTaskImpl.enter(JavacTaskImpl.java:345)
	at jdk.compiler/com.sun.tools.javac.api.JavacTaskImpl.analyze(JavacTaskImpl.java:399)
	at jdk.compiler/com.sun.tools.javac.api.JavacTaskImpl.lambda$analyze$1(JavacTaskImpl.java:379)
	at jdk.compiler/com.sun.tools.javac.api.JavacTaskImpl.invocationHelper(JavacTaskImpl.java:152)
	at jdk.compiler/com.sun.tools.javac.api.JavacTaskImpl.analyze(JavacTaskImpl.java:379)
	... 21 more
tikv-stuff $ 
tikv-stuff $ java -jar tikv-client-java.jar 
Error: Invalid or corrupt jarfile tikv-client-java.jar
tikv-stuff $ file tikv-client-java.jar 
tikv-client-java.jar: XML 1.0 document text, ASCII text
tikv-stuff $ java -jar 
.git/                 explore/              test_raw.java         
README.md             slf4j-api.jar         tikv-client-java.jar  
tikv-stuff $ java -jar slf4j-api.jar 
no main manifest attribute, in slf4j-api.jar
tikv-stuff $ curl -o tikv-client-java.jar https://download.pingcap.org/tikv-client-java-3.2.0-SNAPSHOT.jar && \
> curl -o slf4j-api.jar https://repo1.maven.org/maven2/org/slf4j/slf4j-api/1.7.16/slf4j-api-1.7.16.jar
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100   243    0   243    0     0    190      0 --:--:--  0:00:01 --:--:--   190
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 40509  100 40509    0     0  49887      0 --:--:-- --:--:-- --:--:-- 49826
tikv-stuff $ 
tikv-stuff $ ls -alh
total 104
drwxr-xr-x   8 karuppiahn  staff   256B Aug 28 17:40 .
drwxr-xr-x  19 karuppiahn  staff   608B Aug 28 16:52 ..
drwxr-xr-x  12 karuppiahn  staff   384B Aug 28 16:54 .git
-rw-r--r--   1 karuppiahn  staff    51B Aug 28 16:54 README.md
drwxr-xr-x   3 karuppiahn  staff    96B Aug 28 16:55 explore
-rw-r--r--   1 karuppiahn  staff    40K Aug 28 17:42 slf4j-api.jar
-rw-r--r--   1 karuppiahn  staff   1.3K Aug 28 17:40 test_raw.java
-rw-r--r--   1 karuppiahn  staff   243B Aug 28 17:42 tikv-client-java.jar
tikv-stuff $ cat tikv-client-java.jar 
<?xml version="1.0" encoding="UTF-8"?>
<Error><Code>AccessDenied</Code><Message>Access Denied</Message><RequestId>5XBPKCXQR3WAMQY7</RequestId><HostId>fSlZvm2IPxA+t5255WChMy7siKHxl9HgqkvhRJwAc6antRQrRlc021gwjj1pWoDo5uXzwk3CCQk=</HostId></Error>tikv-stuff $ 
tikv-stuff $ 
tikv-stuff $ 
```

Some wrong JAR or wrong JAR link, hmm

https://download.pingcap.org/tikv-client-java-3.2.0-SNAPSHOT.jar

https://download.pingcap.org/

https://duckduckgo.com/?t=ffab&q=tikv+client+java+jar&ia=software

https://github.com/tikv/client-java

https://github.com/tikv/pd , related repo, placement driver, hmm

https://search.maven.org/

https://search.maven.org/search?q=tikv

https://search.maven.org/search?q=a:tikv-client-java

https://search.maven.org/artifact/org.tikv/tikv-client-java/3.1.2/jar

https://download.pingcap.org/tikv-client-java-3.1.2.jar

https://download.pingcap.org/tikv-client-java-3.1.2-SNAPSHOT.jar

https://search.maven.org/remotecontent?filepath=org/tikv/tikv-client-java/3.1.2/tikv-client-java-3.1.2.jar

```bash
curl -o tikv-client-java.jar https://search.maven.org/remotecontent?filepath=org/tikv/tikv-client-java/3.1.2/tikv-client-java-3.1.2.jar
```

```bash
tikv-stuff $ curl -o tikv-client-java.jar https://search.maven.org/remotecontent?filepath=org/tikv/tikv-client-java/3.1.2/tikv-client-java-3.1.2.jar
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 25.8M  100 25.8M    0     0   924k      0  0:00:28  0:00:28 --:--:-- 3214k
```

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import org.tikv.common.TiConfiguration;
import org.tikv.common.TiSession;
import org.tikv.kvproto.Kvrpcpb;
import org.tikv.raw.RawKVClient;
import org.tikv.shade.com.google.protobuf.ByteString;

TiConfiguration conf = TiConfiguration.createRawDefault("127.0.0.1:2379");
TiSession session = TiSession.create(conf);
RawKVClient client = session.createRawClient();

// put
client.put(ByteString.copyFromUtf8("k1"), ByteString.copyFromUtf8("Hello"));
client.put(ByteString.copyFromUtf8("k2"), ByteString.copyFromUtf8(","));
client.put(ByteString.copyFromUtf8("k3"), ByteString.copyFromUtf8("World"));
client.put(ByteString.copyFromUtf8("k4"), ByteString.copyFromUtf8("!"));
client.put(ByteString.copyFromUtf8("k5"), ByteString.copyFromUtf8("Raw KV"));

// get
Optional<ByteString> result = client.get(ByteString.copyFromUtf8("k1"));
System.out.println(result.get().toStringUtf8());

// batch get
List<Kvrpcpb.KvPair> list =client.batchGet(new ArrayList<ByteString>() {{
add(ByteString.copyFromUtf8("k1"));
add(ByteString.copyFromUtf8("k3"));
}});
System.out.println(list);

// scan
list = client.scan(ByteString.copyFromUtf8("k1"), ByteString.copyFromUtf8("k6"), 10);
System.out.println(list);

// close
client.close();
session.close();
```


```bash
tikv-stuff $ jshell --class-path tikv-client-java.jar:slf4j-api.jar --startup test_raw.java
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
Error:
incompatible types: org.tikv.shade.com.google.protobuf.ByteString cannot be converted to java.util.Optional<org.tikv.shade.com.google.protobuf.ByteString>
Optional<ByteString> result = client.get(ByteString.copyFromUtf8("k1"));
                              ^---------------------------------------^
Error:
cannot find symbol
  symbol:   variable result
System.out.println(result.get().toStringUtf8());
                   ^----^
[key: "k1"
value: "Hello"
, key: "k3"
value: "World"
]
[key: "k1"
value: "Hello"
, key: "k2"
value: ","
, key: "k3"
value: "World"
, key: "k4"
value: "!"
, key: "k5"
value: "Raw KV"
]
|  Welcome to JShell -- Version 16.0.1
|  For an introduction type: /help intro

jshell> 
```

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import org.tikv.common.TiConfiguration;
import org.tikv.common.TiSession;
import org.tikv.kvproto.Kvrpcpb;
import org.tikv.raw.RawKVClient;
import org.tikv.shade.com.google.protobuf.ByteString;

TiConfiguration conf = TiConfiguration.createRawDefault("127.0.0.1:2379");
TiSession session = TiSession.create(conf);
RawKVClient client = session.createRawClient();

// put
client.put(ByteString.copyFromUtf8("k1"), ByteString.copyFromUtf8("Hello"));
client.put(ByteString.copyFromUtf8("k2"), ByteString.copyFromUtf8(","));
client.put(ByteString.copyFromUtf8("k3"), ByteString.copyFromUtf8("World"));
client.put(ByteString.copyFromUtf8("k4"), ByteString.copyFromUtf8("!"));
client.put(ByteString.copyFromUtf8("k5"), ByteString.copyFromUtf8("Raw KV"));

// get
ByteString result = client.get(ByteString.copyFromUtf8("k1"));
System.out.println(result.toStringUtf8());

// batch get
List<Kvrpcpb.KvPair> list =client.batchGet(new ArrayList<ByteString>() {{
add(ByteString.copyFromUtf8("k1"));
add(ByteString.copyFromUtf8("k3"));
}});
System.out.println(list);

// scan
list = client.scan(ByteString.copyFromUtf8("k1"), ByteString.copyFromUtf8("k6"), 10);
System.out.println(list);

// close
client.close();
session.close();
```

```bash
tikv-stuff $ jshell --class-path tikv-client-java.jar:slf4j-api.jar --startup test_raw.java
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
Hello
[key: "k1"
value: "Hello"
, key: "k3"
value: "World"
]
[key: "k1"
value: "Hello"
, key: "k2"
value: ","
, key: "k3"
value: "World"
, key: "k4"
value: "!"
, key: "k5"
value: "Raw KV"
]
|  Welcome to JShell -- Version 16.0.1
|  For an introduction type: /help intro

jshell> 
```

Got some errors for incompatible types. Got rid of optional. Maybe 3.2 has some new feature? Seems to breaking though, going from 3.1 to 3.2, that would be a breaking change to return optional, or maybe it's overloaded? Idk, hmm

Anyways, 3.2.0-snapshot version didn't work, as in, I couldn't even get that version jar

Also, I just chose org.tikv group artifact, there were others too!

com.pingcap.tikv:tikv-client:2.4.1

com.pingcap.tikv:tikv-client-java:3.0.0

Lol. But their time of release was older, compared to org.tikv one

However, https://github.com/tikv/client-java/#use-as-maven-dependency mentions org.tikv group name only, I forgot it though I noticed it, but it was just once

Weird that in the code we use `k6` as one of the keys in the scan

Next, python

```bash
tikv-stuff $ pip3 install -i https://test.pypi.org/simple/ tikv-client

Looking in indexes: https://test.pypi.org/simple/
Collecting tikv-client
  Downloading https://test-files.pythonhosted.org/packages/76/bf/73fd808fe0bdafe428d2b5d0cfb76661108349156a72f80997d68940ba1b/tikv_client-0.1.8-cp39-cp39-macosx_10_7_x86_64.whl (3.0 MB)
     |████████████████████████████████| 3.0 MB 2.2 MB/s 
Installing collected packages: tikv-client
Successfully installed tikv-client-0.1.8
tikv-stuff $ 
```

```bash
tikv-stuff $ python -v
# installing zipimport hook
import zipimport # builtin
# installed zipimport hook
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site.pyc is on a sealed volume, skip mtime check
import site # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/os.pyc is on a sealed volume, skip mtime check
import os # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/os.pyc
import errno # builtin
import posix # builtin
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/posixpath.pyc is on a sealed volume, skip mtime check
import posixpath # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/posixpath.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/stat.pyc is on a sealed volume, skip mtime check
import stat # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/stat.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/genericpath.pyc is on a sealed volume, skip mtime check
import genericpath # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/genericpath.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/warnings.pyc is on a sealed volume, skip mtime check
import warnings # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/warnings.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/linecache.pyc is on a sealed volume, skip mtime check
import linecache # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/linecache.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/types.pyc is on a sealed volume, skip mtime check
import types # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/types.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/UserDict.pyc is on a sealed volume, skip mtime check
import UserDict # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/UserDict.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_abcoll.pyc is on a sealed volume, skip mtime check
import _abcoll # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_abcoll.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/abc.pyc is on a sealed volume, skip mtime check
import abc # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/abc.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_weakrefset.pyc is on a sealed volume, skip mtime check
import _weakrefset # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_weakrefset.pyc
import _weakref # builtin
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/copy_reg.pyc is on a sealed volume, skip mtime check
import copy_reg # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/copy_reg.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/traceback.pyc is on a sealed volume, skip mtime check
import traceback # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/traceback.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sysconfig.pyc is on a sealed volume, skip mtime check
import sysconfig # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sysconfig.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.pyc is on a sealed volume, skip mtime check
import re # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/re.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sre_compile.pyc is on a sealed volume, skip mtime check
import sre_compile # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sre_compile.pyc
import _sre # builtin
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sre_parse.pyc is on a sealed volume, skip mtime check
import sre_parse # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sre_parse.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sre_constants.pyc is on a sealed volume, skip mtime check
import sre_constants # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sre_constants.pyc
dlopen("/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_locale.so", 2);
import _locale # dynamically loaded from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/_locale.so
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_sysconfigdata.pyc is on a sealed volume, skip mtime check
import _sysconfigdata # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_sysconfigdata.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_osx_support.pyc is on a sealed volume, skip mtime check
import _osx_support # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/_osx_support.pyc
import encodings # directory /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings/__init__.pyc is on a sealed volume, skip mtime check
import encodings # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings/__init__.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/codecs.pyc is on a sealed volume, skip mtime check
import codecs # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/codecs.pyc
import _codecs # builtin
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings/aliases.pyc is on a sealed volume, skip mtime check
import encodings.aliases # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings/aliases.pyc
# /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings/utf_8.pyc is on a sealed volume, skip mtime check
import encodings.utf_8 # precompiled from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/encodings/utf_8.pyc

WARNING: Python 2.7 is not recommended. 
This version is included in macOS for compatibility with legacy software. 
Future versions of macOS will not include Python 2.7. 
Instead, it is recommended that you transition to using 'python3' from within Terminal.

Python 2.7.16 (default, Jun 18 2021, 03:23:53) 
[GCC Apple LLVM 12.0.5 (clang-1205.0.19.59.6) [+internal-os, ptrauth-isa=deploy on darwin
Type "help", "copyright", "credits" or "license" for more information.
dlopen("/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/readline.so", 2);
import readline # dynamically loaded from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/readline.so
>>> ^D
# clear __builtin__._
# clear sys.path
# clear sys.argv
# clear sys.ps1
# clear sys.ps2
# clear sys.exitfunc
# clear sys.exc_type
# clear sys.exc_value
# clear sys.exc_traceback
# clear sys.last_type
# clear sys.last_value
# clear sys.last_traceback
# clear sys.path_hooks
# clear sys.path_importer_cache
# clear sys.meta_path
# clear sys.flags
# clear sys.float_info
# restore sys.stdin
# restore sys.stdout
# restore sys.stderr
# cleanup __main__
# cleanup[1] encodings
# cleanup[1] site
# cleanup[1] sysconfig
# cleanup[1] abc
# cleanup[1] _weakrefset
# cleanup[1] sre_constants
# cleanup[1] _codecs
# cleanup[1] _warnings
# cleanup[1] zipimport
# cleanup[1] _sysconfigdata
# cleanup[1] encodings.utf_8
# cleanup[1] _osx_support
# cleanup[1] codecs
# cleanup[1] readline
# cleanup[1] signal
# cleanup[1] traceback
# cleanup[1] posix
# cleanup[1] encodings.aliases
# cleanup[1] exceptions
# cleanup[1] _weakref
# cleanup[1] re
# cleanup[1] _locale
# cleanup[1] sre_compile
# cleanup[1] _sre
# cleanup[1] sre_parse
# cleanup[2] copy_reg
# cleanup[2] posixpath
# cleanup[2] errno
# cleanup[2] _abcoll
# cleanup[2] types
# cleanup[2] genericpath
# cleanup[2] stat
# cleanup[2] warnings
# cleanup[2] UserDict
# cleanup[2] os.path
# cleanup[2] linecache
# cleanup[2] os
# cleanup sys
# cleanup __builtin__
# cleanup ints: 20 unfreed ints
# cleanup floats
tikv-stuff $ python --version
Python 2.7.16
tikv-stuff $ python3 --version
Python 3.9.6
```

```python
from tikv_client import RawClient

client = RawClient.connect("127.0.0.1:2379")

# put
client.put(b"k1", b"Hello")
client.put(b"k2", b",")
client.put(b"k3", b"World")
client.put(b"k4", b"!")
client.put(b"k5", b"Raw KV")

# get
print(client.get(b"k1"))

# batch get
print(client.batch_get([b"k1", b"k3"]))

# scan
print(client.scan(b"k1", end=b"k5", limit=10, include_start=True, include_end=True))
```

```bash
tikv-stuff $ python3 test_raw.py 
b'Hello'
None
[(b'k1', b'Hello'), (b'k2', b','), (b'k3', b'World'), (b'k4', b'!'), (b'k5', b'Raw KV')]
```

Python - weird that it returns `None` for batch get but website shows different output, hmm

```python
from tikv_client import TransactionClient

client = TransactionClient.connect("127.0.0.1:2379")

# put
txn = client.begin()
txn.put(b"k1", b"Hello")
txn.put(b"k2", b",")
txn.put(b"k3", b"World")
txn.put(b"k4", b"!")
txn.put(b"k5", b"TXN KV")
txn.commit()

snapshot = client.snapshot(client.current_timestamp())

# get
print(snapshot.get(b"k1"))

# batch get
print(snapshot.batch_get([b"k1", b"k3"]))

# scan
print(snapshot.scan(b"k1", end=b"k5", limit=10, include_start=True, include_end=True))
```

```bash
tikv-stuff $ python3 test_txn.py 
b'Hello'
[(b'k1', b'Hello'), (b'k3', b'World')]
[(b'k1', b'Hello'), (b'k2', b','), (b'k3', b'World'), (b'k4', b'!'), (b'k5', b'TXN KV')]

tikv-stuff $ python3 test_raw.py 
b'Hello'
None
[(b'k1', b'Hello'), (b'k2', b','), (b'k3', b'World'), (b'k4', b'!'), (b'k5', b'Raw KV')]
tikv-stuff $ 
```

In Transaction API, batch get worked, hmm

I finally stopped everything - clients and also the TiKV server

In the start I did see the prometheus dashboard using http://localhost:9090 and grafana using http://localhost:3000

I guessed grafana usual admin credentials as `admin` and `admin` and later noticed docs had already mentioned it

I didn't see the cluster / TiKV summary actually. There were lots of rows with panels. Gotta check next time [TODO]
