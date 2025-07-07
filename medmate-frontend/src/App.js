import MedicineSearch from "./components/MedicineSearch";
import ReminderForm from "./components/ReminderForm";
import ReminderList from "./components/ReminderList";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function App() {
  return (
    <div className="min-h-screen bg-[#9999CC] p-6" style= {{backgroundImage: `url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='%9999CC' fill-opacity='0.2'%3E%3Cpath d='M0 0h40v40H0z'/%3E%3C/g%3E%3C/svg%3E")`,
}}>
      <ToastContainer />
      
      <h1 className="text-4xl font-extrabold text-center text-white mb-8 flex items-center justify-center gap-2">
        MedMate <span className="text-2xl"></span>
      </h1>

      <div className="bg-[#ECECFF] p-6 rounded-xl shadow-xl mb-6 max-w-4xl mx-auto">
        <h2 className="text-2xl font-bold text-[#3E2B56] mb-4 flex items-center gap-2">
          🔍 Search for Medicines
        </h2>
        <MedicineSearch />
      </div>

      <div className="bg-[#ECECFF] p-6 rounded-xl shadow-xl mb-6 max-w-4xl mx-auto">
        <h2 className="text-2xl font-bold mb-4 text-teal-700 flex items-center gap-2">
          ⏰ Set a Medicine Reminder
        </h2>
        <ReminderForm />
      </div>

      <div className="bg-[#ECECFF] p-6 rounded-xl shadow-xl max-w-4xl mx-auto">
        <h2 className="text-2xl font-bold text-[#3B5BA5] mb-4 flex items-center gap-2">
          📋 Your Reminders
        </h2>
        <ReminderList />
      </div>
    </div>
  );
}

export default App;
