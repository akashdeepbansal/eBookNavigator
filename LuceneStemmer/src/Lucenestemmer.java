import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

import org.tartarus.snowball.ext.PorterStemmer;

public class Lucenestemmer {
	static Set<String> command_dict=new HashSet<String>();
	static ArrayList<String> words_in_dict=new ArrayList<String>();
	
	public static void  main(String args[])
	{
			command_dict.add("skip");
			command_dict.add("move");
			command_dict.add("paragraph");
			
			PorterStemmer stemmer = new PorterStemmer();
			/*
			stemmer.setCurrent("ending"); //set string you need to stem
			stemmer.stem();  //stem the word
			System.out.println(stemmer.getCurrent());//get the stemmed word
			
			stemmer.setCurrent("attaching"); //set string you need to stem
			stemmer.stem();  //stem the word
			System.out.println(stemmer.getCurrent());//get the stemmed word
			
			*/
			String command="Skipping the next paragraph";
			StringTokenizer st=new StringTokenizer(command);
			String cur_word,cur_stem_word;
			String stem_s = "";
			
			while(st.hasMoreTokens())		//Tokenize the String
			{
				cur_word=st.nextToken();
				System.out.print(cur_word);
				cur_word=cur_word.toLowerCase();		//Convert to lower case
				stemmer.setCurrent(cur_word); 			//set string you need to stem
				stemmer.stem();  						//stem the word
				cur_stem_word=stemmer.getCurrent();
				System.out.println(" "+cur_stem_word);
				//stem_s.append(cur_stem_word);
				stem_s+=" "+cur_stem_word;				//Append it to the final command string
				
				
				if(command_dict.contains(cur_stem_word))		//Check if this word exists in our dictionary
				{
					words_in_dict.add(cur_stem_word);
				}
				
			}
			System.out.println("Final Stemmed command is:"+stem_s);
			
			System.out.println("Keywords present in the command are:");
			
			
			for(String s:words_in_dict) {
				System.out.print(s+" ");
				
			}
			
			
			
	}
}
	
	
