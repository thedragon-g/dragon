import QuestionPanel from "@/components/personality-tests/QuestionPanel";
import { data as questions } from "@/app/constants/questions";

const Personality = () => {
	return (
		<section className="h-screen grid place-content-center bg-slate-900">
			<QuestionPanel questions={questions} />
		</section>
	);
};

export default Personality;
