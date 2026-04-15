// Data State
let contacts = JSON.parse(localStorage.getItem('contaxt_pro_data')) || [];

// DOM Elements
const tableBody = document.getElementById('tableBody');
const modal = document.getElementById('contactModal');
const contactForm = document.getElementById('contactForm');

// Initialize
function init() {
    renderContacts(contacts);
}

// Render Table
function renderContacts(dataList) {
    tableBody.innerHTML = '';
    
    if (dataList.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="5" class="p-10 text-center text-zinc-500">No relationships found. Start by adding one.</td></tr>`;
        return;
    }

    dataList.forEach((contact, index) => {
        const tagHTML = contact.tags.split(',').filter(t => t.trim() !== '').map(tag => 
            `<span class="bg-purple-500/10 text-purple-400 text-[9px] px-2 py-1 rounded-md font-bold mr-1 uppercase">${tag.trim()}</span>`
        ).join('');

        const row = `
            <tr class="hover:bg-zinc-800/20 transition group">
                <td class="p-5 font-bold text-zinc-100">${contact.name}</td>
                <td class="p-5 text-zinc-400 text-sm">${contact.company || '—'}</td>
                <td class="p-5 text-zinc-400 text-sm italic">${contact.email || 'No Email'}</td>
                <td class="p-5">${tagHTML || '<span class="text-zinc-700 text-[9px]">NO TAGS</span>'}</td>
                <td class="p-5 text-right">
                    <button onclick="deleteContact(${index})" class="text-zinc-600 hover:text-red-500 transition-colors p-2">
                        <i class="fa-solid fa-trash-can"></i>
                    </button>
                </td>
            </tr>
        `;
        tableBody.innerHTML += row;
    });
}

// Add Contact
contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const newContact = {
        name: document.getElementById('name').value,
        company: document.getElementById('company').value,
        email: document.getElementById('email').value,
        socials: document.getElementById('socials').value,
        tags: document.getElementById('tags').value,
        timestamp: new Date().toISOString()
    };

    contacts.unshift(newContact); // Add to beginning
    saveAndRefresh();
    contactForm.reset();
    closeModal();
});

// Search functionality
function handleSearch() {
    const query = document.getElementById('searchBar').value.toLowerCase();
    const filtered = contacts.filter(c => 
        c.name.toLowerCase().includes(query) || 
        c.company.toLowerCase().includes(query) || 
        c.tags.toLowerCase().includes(query)
    );
    renderContacts(filtered);
}

// Delete functionality
function deleteContact(index) {
    if(confirm('Are you sure you want to remove this relationship?')) {
        contacts.splice(index, 1);
        saveAndRefresh();
    }
}

// Helpers
function saveAndRefresh() {
    localStorage.setItem('contaxt_pro_data', JSON.stringify(contacts));
    renderContacts(contacts);
}

function openModal() { modal.classList.remove('hidden'); }
function closeModal() { modal.classList.add('hidden'); }

// Run on load
init();