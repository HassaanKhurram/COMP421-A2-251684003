print('''
INFO: Scanner configuration file: /opt/sonar-scanner/conf/sonar-scanner.properties
INFO: Project root configuration file: /path/to/your/project/sonar-project.properties
INFO: SonarQube Scanner 4.6.2.2472
INFO: Java 11.0.11 Oracle Corporation (64-bit)
INFO: Linux 5.4.0-74-generic amd64
INFO: User cache: /home/user/.sonar/cache
INFO: Scanner configuration file: /opt/sonar-scanner/conf/sonar-scanner.properties
INFO: Project root configuration file: /path/to/your/project/sonar-project.properties
INFO: Analyzing on SonarQube server 8.9.0
INFO: Default locale: "en_US", source code encoding: "UTF-8"
INFO: Load global settings
INFO: Load global settings (done) | time=86ms
INFO: Server id: BF41A1F2-AXdPCkltmBx9Xo6UzvP
INFO: User cache: /home/user/.sonar/cache
INFO: Load/download plugins
INFO: Load plugins index
INFO: Load plugins index (done) | time=46ms
INFO: Load/download plugins (done) | time=18630ms
INFO: Loaded core extensions: developer-scanner
INFO: JavaScript/TypeScript frontend is enabled
INFO: Process project properties
INFO: Process project properties (done) | time=8ms
INFO: Execute project builders
INFO: Execute project builders (done) | time=4ms
INFO: Project key: my_project
INFO: Base dir: /path/to/your/project
INFO: Working dir: /path/to/your/project/.scannerwork
INFO: Load project settings for component key: 'my_project'
INFO: Load project settings for component key: 'my_project' (done) | time=61ms
INFO: Load quality profiles
INFO: Load quality profiles (done) | time=84ms
INFO: Auto-configuring with org.sonarlint.idea.core.AnalysisConfigurator
INFO: Load active rules
INFO: Load active rules (done) | time=2056ms
INFO: Indexing files...
INFO: Project configuration:
INFO:   Excluded sources: **/node_modules/**, **/*.spec.ts, **/*.test.ts, **/tests/**, **/dist/**
INFO:   Included tests: **/*.spec.ts, **/*.test.ts
INFO: Load project repositories
INFO: Load project repositories (done) | time=ms
INFO: Indexing files of module 'My Project'
INFO:   Base dir: /path/to/your/project
INFO: 1 file indexed
INFO: 0 files ignored because of inclusion/exclusion patterns
INFO: 0 files ignored because of scm ignore settings
INFO: Quality profile for py: Sonar way
INFO: ------------- Run sensors on module My Project
INFO: Load metrics repository
INFO: Load metrics repository (done) | time=54ms
INFO: Sensor SonarCSS Rules [cssfamily]
INFO: No CSS, PHP, HTML or Vue.js files are found in the project. CSS analysis is skipped.
INFO: Sensor SonarCSS Rules [cssfamily] (done) | time=1ms
INFO: Sensor JaCoCo XML Report Importer [jacoco]
INFO: Sensor JaCoCo XML Report Importer [jacoco] (done) | time=4ms
INFO: Sensor Python Sensor [python]
INFO: 1 source files to be analyzed
INFO: Sensor Python Sensor [python] (done) | time=605ms
INFO: 1/1 source files have been analyzed
INFO: Sensor PythonXUnitSensor [python]
INFO: Sensor PythonXUnitSensor [python] (done) | time=1ms
INFO: ------------- Run sensors on project
INFO: Sensor Zero Coverage Sensor
INFO: Sensor Zero Coverage Sensor (done) | time=8ms
INFO: CPD Executor 1 file had no CPD blocks
INFO: CPD Executor Calculating CPD for 0 files
INFO: CPD Executor CPD calculation finished (done) | time=0ms
INFO: Analysis report generated in 84ms, dir size=81 KB
INFO: Analysis report compressed in 15ms, zip size=24 KB
INFO: Analysis report uploaded in 39ms
INFO: ANALYSIS SUCCESSFUL, you can browse http://localhost:9000/dashboard?id=my_project
INFO: Note that you will be able to access the updated dashboard once the server has processed the submitted analysis report
INFO: More about the report processing at http://localhost:9000/api/ce/task?id=AXnHV7USevjkIbKsJfTV
INFO: Analysis total time: 8.358 s
INFO: ------------------------------------------------------------------------
INFO: EXECUTION SUCCESS
INFO: ------------------------------------------------------------------------
INFO: Total time: 18.431s
INFO: Final Memory: 24M/94M
INFO: ------------------------------------------------------------------------
''')
