# Design Verification Checklist

> Use this checklist during and after system design to verify completeness.

## Requirements Traceability

- [ ] All functional requirements mapped to design components
- [ ] Quality attributes ranked and each has a verification strategy
- [ ] Constraints documented and respected in design
- [ ] Invariants explicitly stated and verified

## Structural Soundness

- [ ] Service/component boundaries minimize coupling
- [ ] Each component has single, clear responsibility (cohesion)
- [ ] Data ownership is explicit (no shared mutable state)
- [ ] Data flows traced end-to-end with clear ownership at each stage
- [ ] API contracts defined and versioning strategy specified

## Failure Analysis

- [ ] Every component has a defined failure mode
- [ ] Recovery strategy for each failure mode
- [ ] Cascading failure analysis complete
- [ ] Circuit breaker / bulkhead patterns where needed
- [ ] Graceful degradation defined for non-critical failures

## Security

- [ ] Trust boundaries explicitly drawn
- [ ] Authentication at every trust boundary
- [ ] Authorization model defined (who can do what)
- [ ] Data classification (what is sensitive, where it lives)
- [ ] Encryption at rest and in transit specified
- [ ] Audit logging for security-relevant events

## Observability

- [ ] Every failure mode detectable from monitoring
- [ ] Metrics defined for each quality attribute
- [ ] Distributed tracing across service boundaries
- [ ] Alerting strategy defined (what alerts, who gets them)
- [ ] Runbook/playbook links for each alert

## Scalability

- [ ] Bottleneck component identified
- [ ] Horizontal scaling strategy for each component
- [ ] Capacity limits documented (current and projected)
- [ ] Auto-scaling strategy or manual scaling triggers

## Cost

- [ ] Cost estimated at current load
- [ ] Cost estimated at 10x load
- [ ] Cost estimated at 100x load
- [ ] Most expensive component identified

## Evolution

- [ ] Likely changes identified and design accommodates them
- [ ] Schema evolution strategy for data models
- [ ] API backward compatibility strategy
- [ ] Migration path from current state to proposed design

## Compliance (if applicable)

- [ ] Applicable regulations identified (GDPR, HIPAA, SOC2, etc.)
- [ ] Personal data flows mapped and minimized
- [ ] Data retention policies specified
- [ ] Right to erasure / portability supported (where required)
