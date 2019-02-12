# -*- coding: utf-8 -*-
base_cases = {
    "Base_add_empty_note": {
        "steps": [
            {
                "action": "add_note",
                "text": ""
            }
        ],
        "expected_notes": []
    },
    "Base_add_single_note": {
        "steps": [
            {
                "action": "add_note",
                "text": "Something to do"
            }
        ],
        "expected_notes": [
            {
                "text": "Something to do",
                "status": ""
            }
        ]
    },
    "Base_add_delete_single_note": {
        "steps": [
            {
                "action": "add_note",
                "text": "To be deleted"
            },
            {
                "action": "delete_note",
                "text": "To be deleted"
            }
        ],
        "expected_notes": []
    },
    "Base_add_edit_single_note": {
        "steps": [
            {
                "action": "add_note",
                "text": "To be edited"
            },
            {
                "action": "edit_note",
                "old_text": "To be edited",
                "new_text": "Was edited",
            }
        ],
        "expected_notes": [
            {
                "text": "Was edited",
                "status": ""
            }
        ]
    },
    "Base_add_and_mark_single_note": {
        "steps": [
            {
                "action": "add_note",
                "text": "active to mark complete"
            },
            {
                "action": "mark_note",
                "text": "active to mark complete"
            }
        ],
        "expected_notes": [
            {
                "text": "active to mark complete",
                "status": "completed"
            }
        ]
    },
    "Base_add_mark_delete_single_note": {
        "steps": [
            {
                "action": "add_note",
                "text": "to mark and delete"
            },
            {
                "action": "mark_note",
                "text": "to mark and delete"
            },
            {
                "action": "delete_note",
                "text": "to mark and delete"
            }
        ],
        "expected_notes": []
    },
    "Base_add_mark_edit_single_note": {
        "steps": [
            {
                "action": "add_note",
                "text": "to mark and edit"
            },
            {
                "action": "mark_note",
                "text": "to mark and edit"
            },
            {
                "action": "edit_note",
                "old_text": "to mark and edit",
                "new_text": "was marked and edited",
            }
        ],
        "expected_notes": [
            {
                "text": "was marked and edited",
                "status": "completed"
            }
        ]
    }
}
