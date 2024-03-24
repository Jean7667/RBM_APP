<script>
    document.addEventListener('DOMContentLoaded', function() {
        let skillDropdown = document.getElementById('skill');
        skillDropdown.addEventListener('change', function() {
            let selectedSkill = this.value;
            filterTable(selectedSkill);
        });
    
        function filterTable(selectedSkill) {
            let tableRows = document.querySelectorAll('#expert-table tbody tr');
            tableRows.forEach(function(row) {
                let skillsCell = row.querySelector('td:nth-child(6)');
                let skills = skillsCell.textContent.trim().split(', '); // Split skills by comma and space
                let matchFound = false;
                skills.forEach(function(skill) {
                    if (selectedSkill === '' || skill === selectedSkill) {
                        matchFound = true;
                    }
                });
                if (matchFound) {
                    row.style.display = 'table-row';
                } else {
                    row.style.display = 'none';
                }
            });
        }
    });
    </script>
    