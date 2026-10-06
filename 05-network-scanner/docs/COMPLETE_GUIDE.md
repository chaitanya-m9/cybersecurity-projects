# Complete Project Guide — Network Scanner

## Authorization
Scan only localhost, your own devices, or explicitly authorized systems. Do not use this project for unauthorized reconnaissance or exploitation.

## Abstract
A basic TCP connect scanner for authorized systems and cybersecurity labs. It demonstrates sockets, ports, timeouts, and service exposure.

## Objectives
- Understand TCP ports.
- Implement socket connections.
- Parse port ranges.
- Handle timeouts.
- Report reachable ports.

## Setup and Example
```powershell
cd 05-network-scanner
python src/scanner.py 127.0.0.1 --ports 1-1024
```

## Safe Lab Procedure
1. Start a local test service.
2. Identify its TCP port.
3. Scan only 127.0.0.1.
4. Confirm the service port is reported open.
5. Stop the service.
6. Scan again and compare results.
7. Document the conditions.

## Architecture
CLI → target/range validation → socket creation → TCP connect attempt → result → next port → summary.

## Technical Concepts
A TCP connect scan attempts a normal TCP connection. An open result means the connection was accepted; it does not mean the service is vulnerable.

## Test Plan
| ID | Test | Expected |
|---|---|---|
| NS-01 | Localhost scan | Completes |
| NS-02 | Known local service | Open detected |
| NS-03 | Closed local port | Not open |
| NS-04 | Invalid range | Validation error |
| NS-05 | Unavailable target | Safe error |
| NS-06 | Small range | Fast completion |

## Troubleshooting
- No open ports: start a local test service.
- Timeout: service may be unavailable or filtering.
- Invalid range: use the documented syntax.
- Permission/network policy: remain inside the lab.

## Security
Do not add exploitation, credential attacks, stealth/evasion, or unauthorized discovery. Keep scan intensity conservative.

## Future Enhancements
IPv6, controlled concurrency, JSON output, service identification, configurable timeout, and unit tests.

## Viva Q&A
**What is a port?** A logical endpoint used by network services.
**TCP vs UDP?** TCP is connection-oriented; UDP is connectionless.
**Does an open port mean a vulnerability?** No.
**Why use timeouts?** To prevent indefinite waiting.

## Flowchart
```mermaid
flowchart TD
A[Start]-->B[Read target and ports]
B-->C[Validate]
C-->D[Create TCP socket]
D-->E[Connect]
E-->F{Accepted?}
F-->|Yes|G[Record open]
F-->|No|H[Record closed/unavailable]
G-->I[Next port]
H-->I
I-->J{More ports?}
J-->|Yes|D
J-->|No|K[Display results]
K-->L[End]
```
\n
## Recruiter Review — Sample Input, Output & Technical Evidence

### Controlled Lab Input
Start a local service only on the candidate's own computer:

~~~powershell
python -m http.server 8000 --bind 127.0.0.1
~~~

Then scan the controlled localhost range:

~~~powershell
python src/scanner.py 127.0.0.1 --ports 7995-8005
~~~

### Representative Output
~~~text
Target: 127.0.0.1
Port range: 7995-8005
Scanning...

Open ports:
8000

Scan complete.
~~~

Stop the local service and repeat. The expected result is that port 8000 is no longer reported as open.

### Test Matrix
| Test | Expected |
|---|---|
| Localhost, known service | Open port detected |
| Service stopped | Port not open |
| Closed port | Not reported open |
| Single-port range | Correct result |
| Invalid range | Validation error |
| Timeout/unavailable endpoint | Safe handling |

### Technical Interpretation
An open TCP port means a connection was accepted/reachable during the test. It does **not** mean the service is vulnerable. Vulnerability assessment requires additional authorized analysis.

### What a Recruiter Can Evaluate
- Python socket programming
- TCP fundamentals
- Port concepts
- Timeout handling
- Input validation
- Network-security awareness
- Responsible reconnaissance practices

### Interview Discussion
**Why localhost?** It creates a reproducible and authorization-safe demonstration.

**Why use a timeout?** A scanner should not wait indefinitely for an unresponsive endpoint.

**How could it be improved?** Controlled concurrency, IPv6, service identification, structured output, rate limiting, and automated tests.

### Portfolio Demonstration
The strongest demo is reproducible: start a known local service, detect its port, stop the service, and confirm the result changes.
