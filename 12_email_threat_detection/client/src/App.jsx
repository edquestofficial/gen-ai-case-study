import Form from './Form';
import Quiz from './Quiz';
import Upload_form from './Upload_form';

const App = () => {

  return (
    <>
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-2xl font-bold mb-4">AI Tutor</h1>
        <Form/>
        <Quiz/>
    </div>
     <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-2xl font-bold mb-4">Upload File</h1>
        <Upload_form/>
    </div>
     </>
  );
};

export default App;
