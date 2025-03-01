const subjectsByLevel = {
    foundation: ["ct", "python", "stat1", "stat2", "math1", "math2", "english1", "english2"],
    dip_programming: ["pdsa","dbms","mad1","java","sc","mad2"],
    dip_datascience:["mlf","mlt","mlp","bdm","tds"]
};

const subjectsConfig = {
    python: {
        name: 'python',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'OPPE 1', id: 'pe1', max: 100 },
            { name: 'OPPE 2', id: 'pe2', max: 100 },
            { name: 'GA Average', id: 'gaa1', max: 100 },
            { name: 'GRPA Average', id: 'gaa2', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 },
        ]
    },
    stat1: {
        name: 'Statistics 1',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average', id: 'gaa', max: 100 },
            { name: 'Activity score', id: 'act', max: 5 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    stat2: {
        name: 'Statistics 2',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average', id: 'gaa', max: 100 },
            { name: 'Activity score', id: 'act', max: 5 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    math1: {
        name: 'Mathematics 1',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average', id: 'gaa', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    math2: {
        name: 'Mathematics 2',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average', id: 'gaa', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    english1: {
        name: 'English 1',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average', id: 'gaa', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    english2: {
        name: 'English 2',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average', id: 'gaa', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    ct: {
        name: 'Computational Thinking',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average', id: 'gaa', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },

    pdsa: {
        name: 'PDSA',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'oppe', id: 'pe1', max: 100 },
            { name: 'GA Average', id: 'gaa1', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    dbms: {
        name: 'DBMS',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'oppe', id: 'pe1', max: 100 },
            { name: 'GA Average', id: 'gaa1', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    mad1: {
        name: 'MAD1',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average', id: 'gaa1', max: 100 },
            { name: 'lab GA avg', id: 'gaa2', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    java: {
        name: 'JAVA',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'OPPE 1', id: 'pe1', max: 100 },
            { name: 'OPPE 2', id: 'pe2', max: 100 },
            { name: 'GA Average', id: 'gaa1', max: 100 },
            { name: 'GRPA Average', id: 'gaa2', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 },
        ]
    },

    sc: {
        name: 'SC',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'OPPE', id: 'pe1', max: 100 },
            { name: 'BPT', id: 'pe2', max: 100 },
            { name: 'GA Average', id: 'gaa', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    mad2:  {
        name: 'MAD2',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average', id: 'gaa1', max: 100 },
            { name: 'lab GA avg', id: 'gaa2', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 }
        ]
    },
    mlf: {
        name: 'ML foundation',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average', id: 'gaa1', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 },
        ]
    },
    mlt: {
        name: 'ML techniques',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'GA Average MCQ', id: 'gaa1', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 },
        ]
    },
    mlp: {
        name: 'ML practice',
        components: [
            { name: 'Quiz 1', id: 'quiz1', max: 100 },
            { name: 'OPPE 1', id: 'pe1', max: 100 },
            { name: 'OPPE 2', id: 'pe2', max: 100 },
            { name: 'GA Average', id: 'gaa1', max: 100 },
            { name: 'NPE1', id: 'npe1', max: 100 },
            { name: 'NPE2', id: 'npe2', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 },
        ]
    },
    bdm: {
        name: 'Business Data mang.',
        components: [
            { name: 'Quiz 2', id: 'quiz2', max: 100 },
            { name: 'ROE', id: 'pe1', max: 100 },
            { name: 'GA Average', id: 'gaa1', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 },
        ]
    },
    tds: {
        name: 'tools in DS',
        components: [
            { name: 'ROE', id: 'pe1', max: 100 },
            { name: 'P1', id: 'p1', max: 100 },
            { name: 'P2', id: 'p2', max: 100 },
            { name: 'GA Average', id: 'gaa1', max: 100 },
            { name: 'Bonus', id: 'bonus', max: 2 },
        ]
    },

};

function updateSubjects() {
    const level = document.getElementById("level").value;
    const subjectSelect = document.getElementById("subject");

    subjectSelect.innerHTML = '<option value="">Select Subject</option>'; // Reset options

    if (subjectsByLevel[level]) {
        subjectsByLevel[level].forEach(subjectKey => {
            let option = document.createElement("option");
            option.value = subjectKey;
            option.textContent = subjectsConfig[subjectKey]?.name || subjectKey;
            subjectSelect.appendChild(option);
        });
    }
}

// Updates the form with input fields based on the selected subject
function updateForm() {
    const subject = document.getElementById("subject").value;
    const form = document.getElementById("subjectForm");

    form.innerHTML = ""; // Clear previous inputs

    if (!subject || !subjectsConfig[subject]) return; // Prevent errors
    
    const subjectInput = document.createElement("input");
    subjectInput.type = "hidden";
    subjectInput.name = "subject"; 
    subjectInput.value = subject;
    form.appendChild(subjectInput);

    subjectsConfig[subject].components.forEach(component => {
        const inputDiv = document.createElement("div");
        const input = document.createElement("input");

        input.type = "number";
        input.name = component.id;
        input.id = component.id;
        input.placeholder = component.name;
        input.required = true;
        input.min = 0;
        input.max = component.max;
        input.oninput = function() {
            this.value = Math.min(Math.max(this.value, 0), component.max);
        };

        inputDiv.appendChild(input);
        form.appendChild(inputDiv);
    });
}
document.getElementById("level").addEventListener("change", updateSubjects);
document.getElementById("subject").addEventListener("change", updateForm);