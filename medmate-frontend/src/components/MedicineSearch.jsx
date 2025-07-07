import { useState } from "react";
import axios from "axios";

function MedicineSearch() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    try {
      const res = await axios.get(
        `http://127.0.0.1:8000/medicines/?name=${query.trim().toLowerCase()}`
      );
      setResults(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="p-6 bg-white rounded-xl shadow-lg max-w-xl mx-auto my-6">
      <h2 className="text-2xl font-semibold mb-2 text-[#3E2B56]">Search Medicine</h2>
      
      <div className="flex gap-2">
        <input
          type="text"
          placeholder="Enter medicine name"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") handleSearch();
          }}
          className="flex-1 p-2 border rounded-md"
        />

        <button
          onClick={handleSearch}
          className="bg-[#9999CC] text-white px-4 py-2 rounded hover:bg-[#7a7ab8] focus:outline-none focus:ring-2 focus:ring-[#9999CC] transition"
        >
          Search
        </button>
      </div>

      {results.length === 0 && query && (
        <p className="text-gray-500 mt-4">No medicines found for "{query}"</p>
      )}

      <ul className="mt-4 space-y-2">
        {results.map((med) => (
          <li key={med.id} className="border p-2 rounded shadow-sm bg-blue-50">
            <strong>{med.name}</strong> @ {med.pharmacy}, {med.location}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MedicineSearch;
