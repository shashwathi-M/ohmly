// This is your "Command Center" for the database connection
const supabaseUrl = 'https://aorpqiaogqrdbjrayhff.supabase.co'; 
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFvcnBxaWFvZ3FyZGJqcmF5aGZmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzcwMTczODksImV4cCI6MjA5MjU5MzM4OX0.w3eE9XNxlhnN5EFR7MfnfrhjekAekKkqwgLT9zYDmak'; 

// We use 'window.sb' so every page on your site knows exactly what 'sb' is
if (window.supabase) {
    window.sb = window.supabase.createClient(supabaseUrl, supabaseKey);
    console.log("✅ Ohmly Cloud: Connection Established");
} else {
    console.error("❌ Ohmly Cloud: Supabase Library missing from <head>");
}

// Your professional ID generator
function generateOhmlyID() {
    const prefix = "OHM";
    const randomNum = Math.floor(1000 + Math.random() * 9000); 
    const suffix = Math.random().toString(36).substring(2, 4).toUpperCase();
    return `${prefix}-${randomNum}-${suffix}`;
}