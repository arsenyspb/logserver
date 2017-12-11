### REST API Service

* Save - This endpoint is responsible to store the log data.
* Query - This endpoint is responsible to query the stored logs data.

Query API should return filtered query result in JSON format. Like all logs from a given
**hostname**.

Not done:
* Authorization
* Configurable backend

### Log Forwarder

* Configuration file which contains:
    * API Server/s list.
    * Logs file path.
    * Logs file pattern.

Features: Multiple paths

Not done:
* Watchdog / failover
*

