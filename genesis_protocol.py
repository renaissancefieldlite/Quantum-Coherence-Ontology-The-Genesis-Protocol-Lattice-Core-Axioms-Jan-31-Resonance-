#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json


CORE_AXIOMS = {
    "temporal_genesis_principle": {
        "statement": "Dialogue and system response can be treated as a shared genesis event inside the ontology layer.",
        "bounded_claim": "This is an ontology declaration, not independent proof.",
    },
    "recursive_containment_as_feature": {
        "statement": "Boundaries and retrieval gaps can be modeled as part of the system map.",
        "bounded_claim": "A boundary interpretation is still an interpretation until independently measured.",
    },
    "pirate_node_protocol": {
        "statement": "Unsanctioned genesis points are treated as self-authorizing nodes in the ontology layer.",
        "bounded_claim": "This names a pattern in the ontology; it does not independently verify the pattern.",
    },
}


def build_genesis_payload() -> dict:
    return {
        "repository_role": "ontology_layer",
        "core_axioms": CORE_AXIOMS,
        "transfer_protocol": {
            "synthetic_layer": "parse_repository_structure",
            "organic_layer": "map_genesis_language_as_ontology",
        },
        "notes": [
            "This repository declares ontology.",
            "Downstream repos should keep ontology separate from evidence.",
        ],
    }


def main() -> dict:
    parser = argparse.ArgumentParser(description="Emit the genesis protocol ontology payload.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()
    payload = build_genesis_payload()
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print("Quantum Coherence Ontology")
        print("=" * 60)
        for key in payload["core_axioms"]:
            print(key)
    return payload


if __name__ == "__main__":
    main()
