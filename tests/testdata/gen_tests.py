# -*- coding: utf-8 -*-
gen_cases = {
    "Add_many_notes_and_mark_some": {
        "generated_steps": {
            "active": 5,
            "marked": 3
        },
        "extra_steps": [],
        "expected": {
            "active": 5,
            "marked": 3,
            "bottom": 5
        },
    },
    "Add_and_mark_click_active": {
        "generated_steps": {
            "active": 5,
            "marked": 3
        },
        "extra_steps": [
            {
                "action": "click_active",
            },
        ],
        "expected": {
            "active": 5,
            "marked": 0,
            "bottom": 5
        },
    },
    "Add_and_mark_click_completed": {
        "generated_steps": {
            "active": 5,
            "marked": 3
        },
        "extra_steps": [
            {
                "action": "click_completed",
            },
        ],
        "expected": {
            "active": 0,
            "marked": 3,
            "bottom": 5
        },
    },
    "Clear_from_All": {
        "generated_steps": {
            "active": 5,
            "marked": 3
        },
        "extra_steps": [
            {
                "action": "click_clear",
            },
        ],
        "expected": {
            "active": 5,
            "marked": 0,
            "bottom": 5
        },
    },
    "Clear_from_Completed": {
        "generated_steps": {
            "active": 5,
            "marked": 3
        },
        "extra_steps": [
            {
                "action": "click_completed",
            },
            {
                "action": "click_clear",
            },
        ],
        "expected": {
            "active": 0,
            "marked": 0,
            "bottom": 5
        },
    },
    "Clear_from_Active": {
        "generated_steps": {
            "active": 5,
            "marked": 3
        },
        "extra_steps": [
            {
                "action": "click_active",
            },
            {
                "action": "click_clear",
            },
        ],
        "expected": {
            "active": 5,
            "marked": 0,
            "bottom": 5
        },
    },
    "Save_state_after_refresh": {
        "generated_steps": {
            "active": 3,
            "marked": 2
        },
        "extra_steps": [
            {
                "action": "refresh_page",
            },
        ],
        "expected": {
            "active": 3,
            "marked": 2,
            "bottom": 3
        },
    },
    "Toggle_from_All": {
        "generated_steps": {
            "active": 3,
            "marked": 2
        },
        "extra_steps": [
            {
                "action": "click_toggle_all",
            },
        ],
        "expected": {
            "active": 0,
            "marked": 5,
            "bottom": 0
        },
    },
    "Toggle_from_All_doubleclick": {
        "generated_steps": {
            "active": 3,
            "marked": 2
        },
        "extra_steps": [
            {
                "action": "click_toggle_all",
            },
            {
                "action": "click_toggle_all",
            },
        ],
        "expected": {
            "active": 5,
            "marked": 0,
            "bottom": 5
        },
    },
    "Toggle_from_Active": {
        "generated_steps": {
            "active": 3,
            "marked": 2
        },
        "extra_steps": [
            {
                "action": "click_active",
            },
            {
                "action": "click_toggle_all",
            },
        ],
        "expected": {
            "active": 0,
            "marked": 0,
            "bottom": 0
        },
    },
    "Toggle_from_Active_double_click": {
        "generated_steps": {
            "active": 3,
            "marked": 2
        },
        "extra_steps": [
            {
                "action": "click_active",
            },
            {
                "action": "click_toggle_all",
            },
            {
                "action": "click_toggle_all",
            },
        ],
        "expected": {
            "active": 5,
            "marked": 0,
            "bottom": 5
        },
    },
    "Toggle_from_Complete": {
        "generated_steps": {
            "active": 3,
            "marked": 2
        },
        "extra_steps": [
            {
                "action": "click_completed",
            },
            {
                "action": "click_toggle_all",
            },
        ],
        "expected": {
            "active": 0,
            "marked": 5,
            "bottom": 0
        },
    },
    "Toggle_from_Complete_double_click": {
        "generated_steps": {
            "active": 3,
            "marked": 2
        },
        "extra_steps": [
            {
                "action": "click_completed",
            },
            {
                "action": "click_toggle_all",
            },
            {
                "action": "click_toggle_all",
            },
        ],
        "expected": {
            "active": 0,
            "marked": 0,
            "bottom": 5
        },
    },
}
